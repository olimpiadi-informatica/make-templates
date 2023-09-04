import sys
sys.path.append('..')
from tree import *

reptempl = """
## Formato di input

La prima riga del file di input contiene un intero $%s$, il numero di casi di test. Seguono $%s$ casi di test, numerati da $1$ a $%s$. Ogni caso di test è preceduto da una riga vuota.

Ogni caso di test è composto come segue:

%s

## Formato di output

Il file di output deve contenere la risposta ai casi di test che sei riuscito a risolvere.
Per ogni caso di test che hai risolto, il file di output deve contenere una riga con la dicitura "`%s`",
dove `%s` è il numero del caso di test (a partire da $1$), seguita da%s"""

template = """
## Formato di input

Il file di input è composto come segue:

%s

## Formato di output

Il file di output deve contenere una riga composta da%s"""

locale = {
    'en' : [],
    'it' : []
}

type_dict = {
    'long' : 'long long'
}

itanum = [
    ["", "", "i due", "i tre", "i quattro", "i cinque", "i sei", "i sette", "gli otto", "i nove"],
    ["", "", "le due", "le tre", "le quattro", "le cinque", "le sei", "le sette", "le otto", "le nove"]
]

typegender = {
    'int' : (0, "l'intero", 'interi'),
    'long' : (0, "l'intero a 64 bit", 'interi a 64 bit'),
    'double' : (0, 'il numero con la virgola', 'numeri con la virgola'),
    'char' : (0, 'il carattere', 'caratteri'),
    'string' : (1, 'la stringa', 'stringhe')
}

def type_name(t:str, i:int):
    if i == 1:
        return typegender[t][1]
    return itanum[typegender[t][0]][i] + ' ' + typegender[t][2]

def build_type(t:VarType):
    vals = [x.value for x in t.dims]
    type = t.base
    if type in type_dict:
        type = type_dict[type]
    if len(vals) == 0:
        init = ""
    elif len(vals) == 1:
        init = "(%s)" % vals[0]
    elif len(vals) == 2:
        init = "(%s, vector<%s>(%s))" % (vals[0], type, vals[1])
    else:
        assert False
    for _ in range(len(vals)):
        type = "vector<%s>" % type
    return type, init

def build_reference(r):
    if isinstance(r, str):
        return ("$%s$" if len(r) == 1 else "$\mathtt{%s}$") % r
    assert isinstance(r, VarReference)
    s = r.name
    if len(s) > 1:
        s = "\mathtt{%s}" % s
    if len(r.idx):
        s += "_{%s}" % ','.join(r.idx)
    return "$" + s + "$"

def build_declaration(d:VarDeclaration):
    type, init = build_type(d.type)
    return type + ' ' + ', '.join(n + init for n in d.name) + ';\n'

def build_for(v:str, k:int, b:str, c:str):
    return ("for (int %s = %d; %s %s %s; ++%s)" + (" {\n%s}\n" if c.count('\n') > 1 else "\n%s")) % (v, k, v, "<" if k == 0 else "<=", b, v, c)

def build_inout(types:List[str], refs:List[VarReference]):
    s = ""
    l = []
    for i in range(len(refs)):
        if i == 0 or types[i] != l[-1][0]:
            l.append((types[i], []))
        l[-1][1].append(build_reference(refs[i]))
    l = [type_name(t, len(vars)) + ' ' + ', '.join(vars) for t, vars in l]
    if len(l) == 1:
        s += l[0]
    else:
        s += "; ".join(l[:-1]) + " e " + l[-1]
    return s + ".\n"

def build_sequence(basetype:str, typedims:List[Length], ref:VarReference):
    s = ["gli ", "le "][typegender[basetype][0]]
    s += build_reference(typedims[0].value)
    s += " " + typegender[basetype][2] + " "
    s += build_reference(ref.addIndex('0'))[:-1]
    s += ", \, \ldots, \, "
    ref.idx[-1] = typedims[0].value + "-1"
    s += build_reference(ref)[1:]
    s += ".\n"
    return s

def build_block(prog:Block):
    s = ""
    for c in prog.code:
        if isinstance(c, VarDeclaration):
            pass
        elif isinstance(c, Repeat):
            s += "- " + build_reference(c.bound) + " righe, la " + build_reference(c.idx) +  "-esima contenente "
            if isinstance(c.code.code[0], InOutLine):
                s += build_inout(c.code.code[0].types, c.code.code[0].items)
            elif isinstance(c.code.code[0], InOutSequence):
                s += build_sequence(c.code.code[0].type.base, c.code.code[0].type.dims, c.code.code[0].var)
            else:
                assert False
        elif isinstance(c, InOutSequence):
            s += "- una riga contenente " + build_sequence(c.type.base, c.type.dims, c.var)
        elif isinstance(c, InOutLine):
            s += "- una riga contenente " + build_inout(c.types, c.items)
        elif isinstance(c, FormatLine):
            assert False
        elif isinstance(c, UserCode):
            pass
        elif isinstance(c, Instruction):
            pass
        else:
            raise Exception('Unrecognised instruction "%s"' % c)
    return s

def generate(name:str, prog:Block, lang:str, bounds:dict):
    if isinstance(prog.code[-1], Repeat):
        rep = prog.code[-1]
        fmt = rep.code.code[-2].format[1:-1]
        T = rep.bound
        out = rep.code.code[-1]
        prog.code = rep.code.code[1:-2]
        t = reptempl % (T, T, T, "%s", fmt.replace("{}", rep.idx), rep.idx, "%s")
    else:
        out = prog.code[-1]
        prog.code = prog.code[:-1]
        t = template
    prog = build_block(prog)
    out = build_block(Block(out))[22:]
    if out[:2] == "il":
        out = out[1:]
    elif out[0] == "l":
        out = "l" + out
    return t % (prog, out)
