from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from parser.IOLexer import IOLexer
from parser.IOParser import IOParser
from parser.IOParserVisitor import IOParserVisitor
from tree import *
import targets
import importlib
import argparse
import yaml

# Visitor analysing a parse tree and returning: list of errors, code structure, ?
class Analyzer(IOParserVisitor):
    # Initialize the analyzer.
    def __init__(self):
        self.section = ""
        self.repeatVar = None
        self.definedVars = {'i', 'j'}
        self.loweredVars = {'i', 'j'}


    # Adds a variable in the definition list.
    def defineVar(self, var:str):
        if var.lower() in self.loweredVars:
            self.definedVars.add(var)
            return ['Redefinition of variable "%s"' % var]
        self.definedVars.add(var)
        self.loweredVars.add(var.lower())
        return []


    # Checks that a variable is in the definition list.
    def checkVar(self, var:str):
        if var in self.definedVars:
            return []
        return ['Reference to undefined variable "%s"' % var]


    # Visit a parse tree produced by IOParser#fileSpec.
    def visitFileSpec(self, ctx:IOParser.FileSpecContext):
        err = []
        instr = Block()
        if ctx.REPEAT():
            instr.append(InOutLine(False))
            idx, bound = ctx.IDENT()
            idx = idx.getText()
            bound = bound.getText()
            err += self.defineVar(idx)
            err += self.defineVar(bound)
            self.repeatVar = idx
        ei, i = self.visitInputFile(ctx.inputFile())
        eo, o = self.visitOutputFile(ctx.outputFile())
        instr.append(i)
        instr.append(o)
        if ctx.REPEAT():
            instr = Block(VarDeclaration(VarType('int'), bound), InOutLine(False, ('int', VarReference(bound))), Repeat(idx, 1, bound, instr))
        return err + ei + eo, instr


    # Visit a parse tree produced by IOParser#inputFile.
    def visitInputFile(self, ctx:IOParser.InputFileContext):
        self.section = "input"
        err = []
        block = Block()
        for line in ctx.inputLine():
            el, l = self.visitInputLine(line)
            err += el
            block.append(l)
        return err, block


    # Visit a parse tree produced by IOParser#outputFile.
    def visitOutputFile(self, ctx:IOParser.OutputFileContext):
        self.section = "output"
        err = []
        el, block = self.visitOutputLine(ctx.outputLine())
        instr = block.code[-2]
        block.code = block.code[:-2]
        block.append(Instruction())
        block.append(Instruction())
        block.append(UserCode())
        block.append(Instruction())
        block.append(Instruction())
        if ctx.STR():
            if self.repeatVar is None:
                err.append('Output header formatter is not allowed without a repeat clause: "%s"' % ctx.STR().getText())
            block.append(FormatLine(ctx.STR().getText(), self.repeatVar))
        block.append(instr)
        return err + el, block


    # Visit a parse tree produced by IOParser#inputLine.
    def visitInputLine(self, ctx:IOParser.InputLineContext):
        if ctx.values():
            return self.visitValues(ctx.values())
        elif ctx.vectors():
            return self.visitVectors(ctx.vectors())
        elif ctx.vector():
            return self.visitVector(ctx.vector())
        else:
            return self.visitMatrix(ctx.matrix())


    # Visit a parse tree produced by IOParser#outputLine.
    def visitOutputLine(self, ctx:IOParser.OutputLineContext):
        if ctx.values():
            return self.visitValues(ctx.values())
        else:
            return self.visitVector(ctx.vector())


    # Visit a parse tree produced by IOParser#values.
    def visitValues(self, ctx:IOParser.ValuesContext):
        err = []
        if self.section == "":
            raise Exception("Internal error: undefined section")
        block = Block()
        instr = InOutLine(self.section == "output")
        for c in ctx.homoValues():
            ev, v = self.visitHomoValues(c)
            err += ev
            block.append(v.get(0))
            instr.append(v.get(1))
        block.append(instr)
        block.append(Instruction())
        return err, block


    # Visit a parse tree produced by IOParser#homoValues.
    def visitHomoValues(self, ctx:IOParser.HomoValuesContext):
        err, t = self.visitVarType(ctx.varType())
        ids = []
        for i in ctx.IDENT():
            id = i.getText()
            err += self.defineVar(id)
            ids.append(id)
        type = VarType(t)
        if self.section == "":
            raise Exception("Internal error: undefined section")
        instr = InOutLine(self.section == "output", *[(t, VarReference(id)) for id in ids])
        return err, Block(VarDeclaration(type, *ids), instr)


    # Visit a parse tree produced by IOParser#vectors.
    def visitVectors(self, ctx:IOParser.VectorsContext):
        eb, b = self.visitValues(ctx.values())
        el, l = self.visitArithExpr(ctx.arithExpr())
        if self.section == "":
            raise Exception("Internal error: undefined section")
        for c in b.code[:-2]:
            c.addIndex(l)
        b.code[-2].addIndex('i')
        b.code[-2] = Repeat('i', 0, l.value, Block(b.code[-2]))
        return eb + el, b


    # Visit a parse tree produced by IOParser#vector.
    def visitVector(self, ctx:IOParser.VectorContext):
        id = ctx.IDENT().getText()
        err = self.defineVar(id)
        et, t = self.visitVarType(ctx.varType())
        el, l = self.visitArithExpr(ctx.arithExpr())
        type = VarType(t, l)
        ref = VarReference(id)
        if self.section == "":
            raise Exception("Internal error: undefined section")
        return et + el + err, Block(VarDeclaration(type, id), InOutSequence(self.section == "output", type, ref), Instruction())


    # Visit a parse tree produced by IOParser#matrix.
    def visitMatrix(self, ctx:IOParser.MatrixContext):
        id = ctx.IDENT().getText()
        err = self.defineVar(id)
        et, t = self.visitVarType(ctx.varType())
        en, n = self.visitArithExpr(ctx.arithExpr(0))
        em, m = self.visitArithExpr(ctx.arithExpr(1))
        type = VarType(t, n, m)
        ref = VarReference(id, 'j')
        rep = Repeat('j', 0, n.value, Block(InOutSequence(False, type, ref)))
        return et + en + em + err, Block(VarDeclaration(type, id), rep, Instruction())


    # Visit a parse tree produced by IOParser#varType.
    def visitVarType(self, ctx:IOParser.VarTypeContext):
        return [], ctx.getText()


    # Visit a parse tree produced by IOParser#arithExpr.
    def visitArithExpr(self, ctx:IOParser.ArithExprContext):
        if not ctx.arithExpr():
            return self.visitAddend(ctx.addend())
        err = []
        op = ctx.PLUS() or ctx.MINUS()
        op = ' ' + op.getText() + ' '
        a, b = ctx.arithExpr(), ctx.addend()
        if op == " - ":
            if b.addend() is not None or b.term().NUM() is None:
                err.append('Subtraction by a non-constant expression is forbidden: "%s"' % ctx.getText())
        if a.arithExpr() is None and a.addend().addend() is None and not b.addend() and a.addend().term().NUM() and b.term().NUM():
            err.append('Operations between constants are forbidden: "%s"' % ctx.getText())
        ea, a = self.visitArithExpr(a)
        eb, b = self.visitAddend(b)
        return ea + eb + err, Length(a.value + op + b.value, a.bound + op + b.bound, a.consts | b.consts)


    # Visit a parse tree produced by IOParser#addend.
    def visitAddend(self, ctx:IOParser.AddendContext):
        if not ctx.addend():
            return self.visitTerm(ctx.term())
        err = []
        op = ctx.MULT() or ctx.DIV()
        op = ' ' + op.getText() + ' '
        a, b = ctx.addend(), ctx.term()
        if op == " / ":
            if b.NUM() is None:
                err.append('Division by a non-constant expression is forbidden: "%s"' % ctx.getText())
        if a.addend() is None and a.term().NUM() and b.NUM():
            err.append('Operations between constants are forbidden: "%s"' % ctx.getText())
        ea, a = self.visitAddend(a)
        eb, b = self.visitTerm(b)
        return ea + eb + err, Length(a.value + op + b.value, a.bound + op + b.bound, a.consts | b.consts)


    # Visit a parse tree produced by IOParser#term.
    def visitTerm(self, ctx:IOParser.TermContext):
        err = []
        if ctx.IDENT():
            id = ctx.IDENT().getText()
            err = self.checkVar(id)
            if id != id.upper() or len(id) != 1:
                err.append('Variables used to define array length should be single uppercase letters: "%s"' % id)
            return err, Length(id, 'MAX'+id, set(['MAX'+id]))
        elif ctx.NUM():
            n = ctx.NUM().getText()
            return err, Length(n, n, set())
        else:
            if ctx.arithExpr().addend() and ctx.arithExpr().addend().term():
                err.append('Parentheses around a primitive term are forbidden: "%s"' % ctx.getText())
            l = self.visitArithExpr(ctx.arithExpr())
            l.value = '(' + l.value + ')'
            l.bound = '(' + l.bound + ')'
            return err, l


# Error listener to make sure that parsing errors are not ignored.
class FailOnError(ErrorListener):
    def syntaxError(self, recognizer, offending, line, column, msg, e):
        assert False



def main(args):
    if args.target not in dir(targets):
        print("[ERROR] Target '%s' not supported" % args.target)
        exit(1)

    if args.lang not in ['en', 'it']:
        print("[ERROR] Language '%s' not supported" % args.lang)
        exit(1)

    error_listener = FailOnError()
    input_stream = InputStream(''.join(open(args.spec).readlines()))
    try:
        lexer = IOLexer(input_stream)
        lexer.addErrorListener(error_listener)
        token_stream = CommonTokenStream(lexer)
        parser = IOParser(token_stream)
        parser.addErrorListener(error_listener)
        analyzer = Analyzer()
        err, res = analyzer.visitFileSpec(parser.fileSpec())
    except:
        print("Parsing failed, aborting")
        exit(1)

    for e in err:
        print("[ERROR]", e)

    if len(err) == 0:
        spec = importlib.util.spec_from_file_location('limits', args.limits)
        limits = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(limits)
        name = yaml.safe_load(''.join(open(args.yaml, 'r').readlines()))['name']
        print(getattr(targets, args.target).generate(name, res, args.lang, limits.__dict__))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "spec",
        help="Path of the .spec file",
    )
    parser.add_argument(
        "yaml",
        help="Path of the task.yaml file",
    )
    parser.add_argument(
        "limits",
        help="Path of the limits.py file",
    )
    parser.add_argument(
        "target",
        help="The target language extension (supported: %s)" % ', '.join(x for x in dir(targets) if x[0] != '_'),
    )
    parser.add_argument(
        "lang",
        help="The language of the generated file (supported: en, it)",
    )
    main(parser.parse_args())
