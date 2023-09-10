import sys
sys.path.append('..')
from tree import *

template = """// %s.

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

%s%s
int main() {
    // %s
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);

%s
    return 0;
}
"""

locale = {
    'en' : ["NOTE: it is recommended to use this even if you don't understand the following code", "uncomment the two following lines if you want to read/write from files", "INSERT YOUR CODE HERE"],
    'it' : ["NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente", "decommenta le due righe seguenti se vuoi leggere/scrivere da file", "INSERISCI IL TUO CODICE QUI"]
}

type_dict = {
    'long'   : 'long long'
}

type_formats = {
    'int'    : '%d',
    'long'   : '%lld',
    'double' : '%lf',
    'char'   : '%c',
    'string' : '%s'
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
        type += "[%s]" % v
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
    return ("for (%s = %d; %s %s %s; ++%s)" + (" {\n%s}\n" if c.count('\n') > 1 else "\n%s")) % (v, k, v, "<" if k == 0 else "<=", b, v, c)

def build_inout(out:bool, types:List[str], refs:List[VarReference], end:bool):
    if len(refs) == 0:
        return ""
    s = "printf(\"%s%s\", %s);\n" if out else "assert(" + str(len(refs)) + " == scanf(\"%s%s\", &%s));\n"
    sep = ", " if out else ", &"
    e = "\\n" if out and end else ""
    return s % ("".join(type_formats[t] if t in type_formats else t for t in types), e, sep.join(build_reference(r) for r in refs))

def build_consts(consts:set, bounds:dict):
    if len(consts) == 0:
        return ""
    s = ""
    for c in consts:
        s += "#define %s %s\n" % (c, bounds[c])
    return s + "\n"

def build_vars(vs):
    s = ""
    maxlen = 0
    for type in vs:
        maxlen = max(4 if type == "string" else len(type.split('[')[0]), maxlen)
    for type, vars in vs.items():
        v = list(vars)
        v = sorted([x for x in v if x == x.upper()]) + sorted([x for x in v if x != x.upper()])
        base = type.split('[')[0]
        dims = type[len(base):]
        if base == 'string':
            base = 'char'
            dims += '[MAXS]'
        t = ', '.join(x + dims for x in v)
        s +=  base + ' '*(maxlen+1-len(base)) + t + ';\n'
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
            if 'int' not in vs:
                vs['int'] = set()
            vs['int'].add(c.idx)
            s += build_for(c.idx, c.start,  c.bound, indent(bs))
        elif isinstance(c, InOutSequence):
            if 'int' not in vs:
                vs['int'] = set()
            vs['int'].add('i')
            s += build_for('i', 0, c.type.dims[0].value, indent(build_inout(c.out, [c.type.base], [c.var.addIndex('i')], False)))
        elif isinstance(c, InOutLine):
            s += build_inout(c.out, c.types, c.items, True)
        elif isinstance(c, FormatLine):
            format = c.format[1:-1].replace('{}', '%d')
            s += build_inout(True, [format], [c.var], False)
        elif isinstance(c, UserCode):
            s += "// %s\n" % locale[lang][2]
        elif isinstance(c, Instruction):
            s += "\n"
        else:
            raise Exception('Unrecognised instruction "%s"' % c)
    return cs, vs, s

def generate(name:str, prog:Block, lang:str, bounds:dict):
    bc, bv, bs = build_block(prog, lang)
    if len([t for t in bv if t[:6] == "string"]) > 0:
        bc.add('MAXS')
        if 'MAXS' not in bounds:
            bounds['MAXS'] = 128
    return template % (locale[lang][0], build_consts(bc, bounds), build_vars(bv), locale[lang][1], indent(bs))
