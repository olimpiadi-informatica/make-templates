import sys
sys.path.append('..')
from tree import *

template = """// %s.

import java.util.*;
import java.io.*;
import java.lang.*;

public class %s {

    public static void main(String[] args) throws FileNotFoundException, IOException {
        Locale.setDefault(Locale.US);
        InputStream fin = System.in;
        OutputStream fout = System.out;
        // %s
        // fin = new FileInputStream("input.txt");
        // fout = new FileOutputStream("output.txt");

        Scanner scn = new Scanner(fin);
        PrintStream prnt = new PrintStream(fout);

%s
        fout.flush();
    }
}
"""

locale = {
    'en' : ["NOTE: it is recommended to use this even if you don't understand the following code", "uncomment the two following lines if you want to read/write from files", "INSERT YOUR CODE HERE"],
    'it' : ["NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente", "decommenta le due righe seguenti se vuoi leggere/scrivere da file", "INSERISCI IL TUO CODICE QUI"]
}

type_dict = {
    'string' : 'String'
}

type_vals = {
    'int'    : '0',
    'long'   : '0',
    'double' : '0.0',
    'char'   : "'-'",
    'String' : '""'
}

type_formats = {
    'int'    : '%d',
    'long'   : '%d',
    'double' : '%f',
    'char'   : '%c',
    'string' : '%s'
}

read_dict = {
    'string' : '()',
    'char' : '().charAt(0)'
}

pending_declarations = {}

def build_type(t:VarType):
    vals = [x.value for x in t.dims]
    type = t.base
    if type in type_dict:
        type = type_dict[type]
    if len(vals) == 0:
        init = " = " + type_vals[type]
    else:
        init = " = new " + type + ''.join('[%s]'%v for v in vals)
        type += ''.join('[]' for _ in vals)
    return type, init

def build_reference(r):
    if isinstance(r, str):
        return r
    assert isinstance(r, VarReference)
    return r.name + ''.join('[%s]' % i for i in r.idx)

def build_declaration(d:VarDeclaration):
    type, init = build_type(d.type)
    return type + ' ' + ', '.join(n + init for n in d.name) + ';\n'

def build_for(v:str, k:int, b:str, c:str):
    return ("for (int %s = %d; %s %s %s; ++%s)" + (" {\n%s}\n" if c.count('\n') > 1 else "\n%s")) % (v, k, v, "<" if k == 0 else "<=", b, v, c)

def build_inout(out:bool, types:List[str], refs:List[VarReference], end:bool):
    if len(refs) == 0 and not (out and end):
        return ""
    if out:
        fmt = '"%s%s"' % (" ".join(type_formats[t] if t in type_formats else t for t in types), "\\n" if end else " " if types[0] in type_formats else "")
        return "prnt.format(%s);\n" % ", ".join([fmt] + [build_reference(r) for r in refs])
    s = ""
    for i in range(len(types)):
        t = types[i]
        r = refs[i]
        s += pending_declarations[r.name] + build_reference(r) + " = scn.next" + (read_dict[t] if t in read_dict else t.capitalize()+'()') + ";\n"
    return s

def build_block(prog:Block, lang:str):
    s = ""
    for i in range(len(prog.code)):
        c = prog.code[i]
        if isinstance(c, VarDeclaration):
            j = i+1
            while isinstance(prog.code[j], VarDeclaration):
                j = j+1
            if len(c.type.dims) > 0 or not isinstance(prog.code[j], InOutLine):
                s += build_declaration(c)
                for n in c.name:
                    pending_declarations[n] = ""
            else:
                t = build_type(c.type)[0] + " "
                for n in c.name:
                    pending_declarations[n] = t
        elif isinstance(c, Repeat):
            s += build_for(c.idx, c.start,  c.bound, indent(build_block(c.code, lang)))
        elif isinstance(c, InOutSequence):
            s += build_for('i', 0, c.type.dims[-1].value, indent(build_inout(c.out, [c.type.base], [c.var.addIndex('i')], False)))
            s += build_inout(c.out, [], [], True)
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
    return s

def generate(name:str, prog:Block, lang:str, bounds:dict):
    return template % (locale[lang][0], name, locale[lang][1], indent(indent(build_block(prog, lang))))
