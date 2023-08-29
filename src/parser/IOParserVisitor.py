# Generated from /Users/harniver/Git/olimpiadi/slide/grammar/IOParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IOParser import IOParser
else:
    from IOParser import IOParser

# This class defines a complete generic visitor for a parse tree produced by IOParser.

class IOParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IOParser#filespec.
    def visitFilespec(self, ctx:IOParser.FilespecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#inputfile.
    def visitInputfile(self, ctx:IOParser.InputfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#outputfile.
    def visitOutputfile(self, ctx:IOParser.OutputfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#inputline.
    def visitInputline(self, ctx:IOParser.InputlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#headerline.
    def visitHeaderline(self, ctx:IOParser.HeaderlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#outputline.
    def visitOutputline(self, ctx:IOParser.OutputlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#values.
    def visitValues(self, ctx:IOParser.ValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#homoValues.
    def visitHomoValues(self, ctx:IOParser.HomoValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#vectors.
    def visitVectors(self, ctx:IOParser.VectorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#vector.
    def visitVector(self, ctx:IOParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#matrix.
    def visitMatrix(self, ctx:IOParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#vartype.
    def visitVartype(self, ctx:IOParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#arithExpr.
    def visitArithExpr(self, ctx:IOParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#addend.
    def visitAddend(self, ctx:IOParser.AddendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IOParser#term.
    def visitTerm(self, ctx:IOParser.TermContext):
        return self.visitChildren(ctx)



del IOParser