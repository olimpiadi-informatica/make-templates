import sys
sys.path.append('..')
from ..tree import *

template = """// %s.

%s"""

locale = {
    'en' : ["NOTE: it is recommended to use this even if you don't understand the following code", "INSERT YOUR CODE HERE"],
    'it' : ["NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente", "INSERISCI IL TUO CODICE QUI"]
}

type_vals = {
    'int'    : '0',
    'long'   : '0',
    'double' : '0.0',
    'char'   : "'-'",
    'string' : "''"
}

type_read = {
    'int'    : 'Int',
    'long'   : 'Int',
    'double' : 'Float',
    'char'   : 'Char',
    'string' : 'String'
}

pending_declarations = {}

input_vars = []
output_vars = []

def get_output_vars():
    return output_vars[0] if len(output_vars) == 1 else "[%s]" % (', '.join(output_vars))

def build_type(t:VarType):
    vals = [x.value for x in t.dims]
    if len(vals) == 0:
        init = " = " + type_vals[t.base]
    elif len(vals) == 1:
        init = " = Array(%s)" % vals[0]
    else:
        assert(len(vals) == 2)
        init = " = Array.from(Array(%s), () => Array(%s))" % tuple(vals)
    return init

def build_reference(r):
    if isinstance(r, str):
        return r
    assert isinstance(r, VarReference)
    return r.name + ''.join('[%s]' % i for i in r.idx)

def build_declaration(d:VarDeclaration):
    init = build_type(d.type)
    if len(d.type.dims) > 0:
        return '\n'.join('let %s%s;' % (n, init) for n in d.name) + '\n'
    return 'let ' + ', '.join(n + init for n in d.name) + ';\n'

def build_for(v:str, k:int, b:str, c:str):
    return ("for (let %s = %d; %s %s %s; ++%s)" + (" {\n%s}\n" if c.count('\n') > 1 else "\n%s")) % (v, k, v, "<" if k == 0 else "<=", b, v, c)

def build_inout(out:bool, types:List[str], refs:List[VarReference], end:bool):
    if len(refs) == 0 and not (out and end):
        return ""
    if out:
        s = " ".join(("${%s}" % build_reference(r)) for r in refs)
        if end is not None:
            s += ('\\r\\n' if end else ' ')
        return "writeln(`%s`);\n" % s
    s = ""
    for i in range(len(types)):
        t = types[i]
        r = refs[i]
        s += pending_declarations[r.name] + build_reference(r) + " = read" + type_read[t] + "();\n"
    return s

def build_block(prog:Block, lang:str):
    global input_vars, output_vars
    s = ""
    u = ""
    outsec = False
    for i in range(len(prog.code)):
        c = prog.code[i]
        if isinstance(c, VarDeclaration):
            j = i+1
            while isinstance(prog.code[j], VarDeclaration):
                j = j+1
            is_input = isinstance(prog.code[j], InOutLine) or isinstance(prog.code[j], InOutSequence) or isinstance(prog.code[j], Repeat)
            if is_input:
                input_vars += c.name
            else:
                output_vars += c.name
            if len(c.type.dims) > 0 or not isinstance(prog.code[j], InOutLine):
                if is_input:
                    s += build_declaration(c)
                else:
                    s += build_declaration(c)
                for n in c.name:
                    pending_declarations[n] = ""
            else:
                for n in c.name:
                    pending_declarations[n] = "let "
        elif isinstance(c, Repeat):
            ss = build_block(c.code, lang)
            temp = build_for(c.idx, c.start,  c.bound, indent(ss))
            if outsec:
                u += temp
            else:
                s += temp
        elif isinstance(c, InOutSequence):
            temp = build_for('i', 0, c.type.dims[-1].value, indent(build_inout(c.out, [c.type.base], [c.var.addIndex('i')], False)))
            temp += build_inout(c.out, [], [], True)
            if outsec and c.out:
                u += temp
            else:
                s += temp
        elif isinstance(c, InOutLine):
            temp = build_inout(c.out, c.types, c.items, True)
            if outsec and c.out:
                u += temp
            else:
                s += temp
        elif isinstance(c, FormatLine):
            u += "writeln(`%s`);\n" % c.format[1:-1].replace('{}', '${%s}' % c.var)
        elif isinstance(c, UserCode):
            outsec = True
            u += "// %s\n\n" % locale[lang][1]
        elif isinstance(c, Instruction):
            if len(s) < 2 or s[-2] != '\n':
                s += '\n'
        else:
            raise Exception('Unrecognised instruction "%s"' % c)
    if len(u):
        s += u
    return s

def generate(name:str, prog:Block, lang:str, bounds:dict):
    code = build_block(prog, lang)
    return template % (locale[lang][0], code)
