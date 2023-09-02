import sys
sys.path.append('..')
from tree import *

template = """{ %s }

%s%s
begin
{
    %s
    assign(input,  'input.txt');  reset(input);
    assign(output, 'output.txt'); rewrite(output);
}

%s
end.
"""

locale = {
    'en' : ["NOTE: it is recommended to use this even if you don't understand the following code", "uncomment the two following lines if you want to read/write from files", "INSERT YOUR CODE HERE"],
    'it' : ["NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente", "decommenta le due righe seguenti se vuoi leggere/scrivere da file", "INSERISCI IL TUO CODICE QUI"]
}

type_dict = {
    'int'  : 'LongInt',
    'long' : 'Int64',
    'double' : 'Double',
    'char'  : 'Char',
    'string' : 'AnsiString'
}

def build_type(t:VarType):
    consts = set()
    for x in t.dims:
        consts |= x.consts
    vals = [x.bound for x in t.dims]
    type = t.base
    if type in type_dict:
        type = type_dict[type]
    for v in vals:
        type = "Array[0..%s-1] of " % v + type
    return type, consts

def build_reference(r):
    if isinstance(r, str):
        return r
    assert isinstance(r, VarReference)
    return r.name + ''.join('[%s]' % i for i in r.idx)

def build_declaration(d:VarDeclaration):
    type, consts = build_type(d.type)
    return consts, type, d.name

def build_for(v:str, k:int, b:str, c:str):
    return ("for %s:=%d to %s do" + (" begin\n%send;\n" if c.count('\n') > 1 else "\n%s")) % (v, k, b + ("-1" if k == 0 else ""), c)

def build_inout(out:bool, refs:List[VarReference], end:bool):
    cmd = ("Write" if out else "Read") + ("Ln" if end else "")
    return cmd + '(' + ', '.join(build_reference(r) for r in refs) + ');\n'

def build_consts(consts:set, bounds:dict):
    if len(consts) == 0:
        return ""
    s = ""
    for c in consts:
        s += "%s = %s;\n" % (c, bounds[c])
    return "const\n" + indent(s) + "\n"

def build_vars(vs):
    s = ""
    maxlen = 0
    for type, vars in vs.items():
        maxlen = max(len(', '.join(vars)), maxlen)
    for type, vars in vs.items():
        v = list(vars)
        t = ', '.join(sorted([x for x in v if x == x.upper()]) + sorted([x for x in v if x != x.upper()]))
        s += t + ' '*(maxlen - len(t)) + ' : ' + type + ';\n'
    s = "var\n" + indent(s)
    return s

def build_block(prog:Block, lang:str):
    cs = set()
    vs = {}
    s = ""
    for c in prog.code:
        if isinstance(c, VarDeclaration):
            consts, type, ids = build_declaration(c)
            cs |= consts
            if type not in vs:
                vs[type] = set()
            vs[type] |= set(ids)
        elif isinstance(c, Repeat):
            bc, bv, bs = build_block(c.code, lang)
            cs |= bc
            vs.update(bv)
            if 'LongInt' not in vs:
                vs['LongInt'] = set()
            vs['LongInt'].add(c.idx)
            s += build_for(c.idx, c.start,  c.bound, indent(bs))
        elif isinstance(c, InOutSequence):
            if 'LongInt' not in vs:
                vs['LongInt'] = set()
            vs['LongInt'].add('i')
            s += build_for('i', 0, c.type.dims[0].value, indent(build_inout(c.out, [c.var.addIndex('i')], False)))
            s += build_inout(c.out, [], True)
        elif isinstance(c, InOutLine):
            s += build_inout(c.out, c.items, True)
        elif isinstance(c, FormatLine):
            format = c.format[1:-1].split('{}')
            s += build_inout(True, ['"%s"'%format[0], c.var, '"%s"'%format[1]], False)
        elif isinstance(c, UserCode):
            s = s[:-1] + "{ %s }\n" % locale[lang][2]
        elif isinstance(c, Instruction):
            s += "\n"
        else:
            raise Exception('Unrecognised instruction "%s"' % c)
    return cs, vs, s

def generate(name:str, prog:Block, lang:str, bounds:dict):
    bc, bv, bs = build_block(prog, lang)
    return template % (locale[lang][0], build_consts(bc, bounds), build_vars(bv), locale[lang][1], indent(bs))
