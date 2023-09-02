# Generated from /Users/harniver/Git/olimpiadi/slide/grammar/IOParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u00b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\5\2+\n\2\3\2\7\2.\n\2\f\2\16\2\61\13\2")
        buf.write("\3\2\3\2\6\2\65\n\2\r\2\16\2\66\3\2\3\2\7\2;\n\2\f\2\16")
        buf.write("\2>\13\2\3\2\3\2\3\3\3\3\3\3\6\3E\n\3\r\3\16\3F\3\3\3")
        buf.write("\3\6\3K\n\3\r\3\16\3L\3\3\7\3P\n\3\f\3\16\3S\13\3\3\4")
        buf.write("\3\4\3\4\6\4X\n\4\r\4\16\4Y\3\4\3\4\6\4^\n\4\r\4\16\4")
        buf.write("_\5\4b\n\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5j\n\5\3\6\3\6\5")
        buf.write("\6n\n\6\3\7\3\7\3\7\6\7s\n\7\r\7\16\7t\3\b\3\b\3\b\3\b")
        buf.write("\7\b{\n\b\f\b\16\b~\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\7\r\u00a1\n\r\f\r\16\r\u00a4\13\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\7\16\u00ac\n\16\f\16\16\16\u00af\13\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b7\n\17\3\17\2")
        buf.write("\4\30\32\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\5\3")
        buf.write("\2\3\7\3\2\b\t\3\2\n\13\2\u00bf\2!\3\2\2\2\4A\3\2\2\2")
        buf.write("\6T\3\2\2\2\bi\3\2\2\2\nm\3\2\2\2\fr\3\2\2\2\16v\3\2\2")
        buf.write("\2\20\177\3\2\2\2\22\u0087\3\2\2\2\24\u008e\3\2\2\2\26")
        buf.write("\u0098\3\2\2\2\30\u009a\3\2\2\2\32\u00a5\3\2\2\2\34\u00b6")
        buf.write("\3\2\2\2\36 \7\25\2\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2")
        buf.write("\2\2!\"\3\2\2\2\"*\3\2\2\2#!\3\2\2\2$%\7\26\2\2%&\7\37")
        buf.write("\2\2&\'\7\27\2\2\'(\7\37\2\2()\7\23\2\2)+\7\25\2\2*$\3")
        buf.write("\2\2\2*+\3\2\2\2+/\3\2\2\2,.\7\25\2\2-,\3\2\2\2.\61\3")
        buf.write("\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62\3\2\2\2\61/\3\2\2\2")
        buf.write("\62\64\5\4\3\2\63\65\7\25\2\2\64\63\3\2\2\2\65\66\3\2")
        buf.write("\2\2\66\64\3\2\2\2\66\67\3\2\2\2\678\3\2\2\28<\5\6\4\2")
        buf.write("9;\7\25\2\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=?")
        buf.write("\3\2\2\2><\3\2\2\2?@\7\2\2\3@\3\3\2\2\2AB\7\30\2\2BD\7")
        buf.write("\23\2\2CE\7\25\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2")
        buf.write("\2\2GH\3\2\2\2HQ\5\b\5\2IK\7\25\2\2JI\3\2\2\2KL\3\2\2")
        buf.write("\2LJ\3\2\2\2LM\3\2\2\2MN\3\2\2\2NP\5\b\5\2OJ\3\2\2\2P")
        buf.write("S\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\5\3\2\2\2SQ\3\2\2\2TU\7")
        buf.write("\31\2\2UW\7\23\2\2VX\7\25\2\2WV\3\2\2\2XY\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Za\3\2\2\2[]\7\35\2\2\\^\7\25\2\2]\\\3")
        buf.write("\2\2\2^_\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a[\3\2\2")
        buf.write("\2ab\3\2\2\2bc\3\2\2\2cd\5\n\6\2d\7\3\2\2\2ej\5\f\7\2")
        buf.write("fj\5\20\t\2gj\5\22\n\2hj\5\24\13\2ie\3\2\2\2if\3\2\2\2")
        buf.write("ig\3\2\2\2ih\3\2\2\2j\t\3\2\2\2kn\5\f\7\2ln\5\22\n\2m")
        buf.write("k\3\2\2\2ml\3\2\2\2n\13\3\2\2\2op\5\16\b\2pq\7\24\2\2")
        buf.write("qs\3\2\2\2ro\3\2\2\2st\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\r")
        buf.write("\3\2\2\2vw\5\26\f\2w|\7\37\2\2xy\7\22\2\2y{\7\37\2\2z")
        buf.write("x\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\17\3\2\2\2~|")
        buf.write("\3\2\2\2\177\u0080\7\20\2\2\u0080\u0081\5\f\7\2\u0081")
        buf.write("\u0082\7\21\2\2\u0082\u0083\7\16\2\2\u0083\u0084\5\30")
        buf.write("\r\2\u0084\u0085\7\17\2\2\u0085\u0086\7\24\2\2\u0086\21")
        buf.write("\3\2\2\2\u0087\u0088\5\26\f\2\u0088\u0089\7\37\2\2\u0089")
        buf.write("\u008a\7\16\2\2\u008a\u008b\5\30\r\2\u008b\u008c\7\17")
        buf.write("\2\2\u008c\u008d\7\24\2\2\u008d\23\3\2\2\2\u008e\u008f")
        buf.write("\5\26\f\2\u008f\u0090\7\37\2\2\u0090\u0091\7\16\2\2\u0091")
        buf.write("\u0092\5\30\r\2\u0092\u0093\7\17\2\2\u0093\u0094\7\16")
        buf.write("\2\2\u0094\u0095\5\30\r\2\u0095\u0096\7\17\2\2\u0096\u0097")
        buf.write("\7\24\2\2\u0097\25\3\2\2\2\u0098\u0099\t\2\2\2\u0099\27")
        buf.write("\3\2\2\2\u009a\u009b\b\r\1\2\u009b\u009c\5\32\16\2\u009c")
        buf.write("\u00a2\3\2\2\2\u009d\u009e\f\3\2\2\u009e\u009f\t\3\2\2")
        buf.write("\u009f\u00a1\5\32\16\2\u00a0\u009d\3\2\2\2\u00a1\u00a4")
        buf.write("\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\31\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\b\16\1\2\u00a6")
        buf.write("\u00a7\5\34\17\2\u00a7\u00ad\3\2\2\2\u00a8\u00a9\f\3\2")
        buf.write("\2\u00a9\u00aa\t\4\2\2\u00aa\u00ac\5\34\17\2\u00ab\u00a8")
        buf.write("\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\33\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0")
        buf.write("\u00b7\7\37\2\2\u00b1\u00b7\7\36\2\2\u00b2\u00b3\7\f\2")
        buf.write("\2\u00b3\u00b4\5\30\r\2\u00b4\u00b5\7\r\2\2\u00b5\u00b7")
        buf.write("\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b1\3\2\2\2\u00b6")
        buf.write("\u00b2\3\2\2\2\u00b7\35\3\2\2\2\24!*/\66<FLQY_aimt|\u00a2")
        buf.write("\u00ad\u00b6")
        return buf.getvalue()


class IOParser ( Parser ):

    grammarFileName = "IOParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'long'", "'double'", "'char'", 
                     "'string'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'", "','", "':'", "';'", "'\n'", 
                     "'repeat'", "'upto'", "'input'", "'output'" ]

    symbolicNames = [ "<INVALID>", "INT", "LONG", "DOUBLE", "CHAR", "STRING", 
                      "PLUS", "MINUS", "MULT", "DIV", "LPAREN", "RPAREN", 
                      "LBRACK", "RBRACK", "LBRACE", "RBRACE", "COMMA", "COLON", 
                      "SEMICOL", "NL", "REPEAT", "UPTO", "INPUT", "OUTPUT", 
                      "WS", "INLINE_COMMENT", "BLOCK_COMMENT", "STR", "NUM", 
                      "IDENT" ]

    RULE_fileSpec = 0
    RULE_inputFile = 1
    RULE_outputFile = 2
    RULE_inputLine = 3
    RULE_outputLine = 4
    RULE_values = 5
    RULE_homoValues = 6
    RULE_vectors = 7
    RULE_vector = 8
    RULE_matrix = 9
    RULE_varType = 10
    RULE_arithExpr = 11
    RULE_addend = 12
    RULE_term = 13

    ruleNames =  [ "fileSpec", "inputFile", "outputFile", "inputLine", "outputLine", 
                   "values", "homoValues", "vectors", "vector", "matrix", 
                   "varType", "arithExpr", "addend", "term" ]

    EOF = Token.EOF
    INT=1
    LONG=2
    DOUBLE=3
    CHAR=4
    STRING=5
    PLUS=6
    MINUS=7
    MULT=8
    DIV=9
    LPAREN=10
    RPAREN=11
    LBRACK=12
    RBRACK=13
    LBRACE=14
    RBRACE=15
    COMMA=16
    COLON=17
    SEMICOL=18
    NL=19
    REPEAT=20
    UPTO=21
    INPUT=22
    OUTPUT=23
    WS=24
    INLINE_COMMENT=25
    BLOCK_COMMENT=26
    STR=27
    NUM=28
    IDENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputFile(self):
            return self.getTypedRuleContext(IOParser.InputFileContext,0)


        def outputFile(self):
            return self.getTypedRuleContext(IOParser.OutputFileContext,0)


        def EOF(self):
            return self.getToken(IOParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.NL)
            else:
                return self.getToken(IOParser.NL, i)

        def REPEAT(self):
            return self.getToken(IOParser.REPEAT, 0)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.IDENT)
            else:
                return self.getToken(IOParser.IDENT, i)

        def UPTO(self):
            return self.getToken(IOParser.UPTO, 0)

        def COLON(self):
            return self.getToken(IOParser.COLON, 0)

        def getRuleIndex(self):
            return IOParser.RULE_fileSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileSpec" ):
                return visitor.visitFileSpec(self)
            else:
                return visitor.visitChildren(self)




    def fileSpec(self):

        localctx = IOParser.FileSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_fileSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self.match(IOParser.NL) 
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IOParser.REPEAT:
                self.state = 34
                self.match(IOParser.REPEAT)
                self.state = 35
                self.match(IOParser.IDENT)
                self.state = 36
                self.match(IOParser.UPTO)
                self.state = 37
                self.match(IOParser.IDENT)
                self.state = 38
                self.match(IOParser.COLON)
                self.state = 39
                self.match(IOParser.NL)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IOParser.NL:
                self.state = 42
                self.match(IOParser.NL)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.inputFile()
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.match(IOParser.NL)
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IOParser.NL):
                    break

            self.state = 54
            self.outputFile()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IOParser.NL:
                self.state = 55
                self.match(IOParser.NL)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(IOParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(IOParser.INPUT, 0)

        def COLON(self):
            return self.getToken(IOParser.COLON, 0)

        def inputLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.InputLineContext)
            else:
                return self.getTypedRuleContext(IOParser.InputLineContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.NL)
            else:
                return self.getToken(IOParser.NL, i)

        def getRuleIndex(self):
            return IOParser.RULE_inputFile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputFile" ):
                return visitor.visitInputFile(self)
            else:
                return visitor.visitChildren(self)




    def inputFile(self):

        localctx = IOParser.InputFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_inputFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(IOParser.INPUT)
            self.state = 64
            self.match(IOParser.COLON)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.match(IOParser.NL)
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IOParser.NL):
                    break

            self.state = 70
            self.inputLine()
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 72 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 71
                        self.match(IOParser.NL)
                        self.state = 74 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==IOParser.NL):
                            break

                    self.state = 76
                    self.inputLine() 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputFileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(IOParser.OUTPUT, 0)

        def COLON(self):
            return self.getToken(IOParser.COLON, 0)

        def outputLine(self):
            return self.getTypedRuleContext(IOParser.OutputLineContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.NL)
            else:
                return self.getToken(IOParser.NL, i)

        def STR(self):
            return self.getToken(IOParser.STR, 0)

        def getRuleIndex(self):
            return IOParser.RULE_outputFile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputFile" ):
                return visitor.visitOutputFile(self)
            else:
                return visitor.visitChildren(self)




    def outputFile(self):

        localctx = IOParser.OutputFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_outputFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(IOParser.OUTPUT)
            self.state = 83
            self.match(IOParser.COLON)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.match(IOParser.NL)
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IOParser.NL):
                    break

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IOParser.STR:
                self.state = 89
                self.match(IOParser.STR)
                self.state = 91 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 90
                    self.match(IOParser.NL)
                    self.state = 93 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==IOParser.NL):
                        break



            self.state = 97
            self.outputLine()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def values(self):
            return self.getTypedRuleContext(IOParser.ValuesContext,0)


        def vectors(self):
            return self.getTypedRuleContext(IOParser.VectorsContext,0)


        def vector(self):
            return self.getTypedRuleContext(IOParser.VectorContext,0)


        def matrix(self):
            return self.getTypedRuleContext(IOParser.MatrixContext,0)


        def getRuleIndex(self):
            return IOParser.RULE_inputLine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputLine" ):
                return visitor.visitInputLine(self)
            else:
                return visitor.visitChildren(self)




    def inputLine(self):

        localctx = IOParser.InputLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inputLine)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.values()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.vectors()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.vector()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 102
                self.matrix()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def values(self):
            return self.getTypedRuleContext(IOParser.ValuesContext,0)


        def vector(self):
            return self.getTypedRuleContext(IOParser.VectorContext,0)


        def getRuleIndex(self):
            return IOParser.RULE_outputLine

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputLine" ):
                return visitor.visitOutputLine(self)
            else:
                return visitor.visitChildren(self)




    def outputLine(self):

        localctx = IOParser.OutputLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_outputLine)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.values()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.vector()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def homoValues(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.HomoValuesContext)
            else:
                return self.getTypedRuleContext(IOParser.HomoValuesContext,i)


        def SEMICOL(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.SEMICOL)
            else:
                return self.getToken(IOParser.SEMICOL, i)

        def getRuleIndex(self):
            return IOParser.RULE_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValues" ):
                return visitor.visitValues(self)
            else:
                return visitor.visitChildren(self)




    def values(self):

        localctx = IOParser.ValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 109
                self.homoValues()
                self.state = 110
                self.match(IOParser.SEMICOL)
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IOParser.INT) | (1 << IOParser.LONG) | (1 << IOParser.DOUBLE) | (1 << IOParser.CHAR) | (1 << IOParser.STRING))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HomoValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(IOParser.VarTypeContext,0)


        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.IDENT)
            else:
                return self.getToken(IOParser.IDENT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.COMMA)
            else:
                return self.getToken(IOParser.COMMA, i)

        def getRuleIndex(self):
            return IOParser.RULE_homoValues

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHomoValues" ):
                return visitor.visitHomoValues(self)
            else:
                return visitor.visitChildren(self)




    def homoValues(self):

        localctx = IOParser.HomoValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_homoValues)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.varType()
            self.state = 117
            self.match(IOParser.IDENT)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IOParser.COMMA:
                self.state = 118
                self.match(IOParser.COMMA)
                self.state = 119
                self.match(IOParser.IDENT)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(IOParser.LBRACE, 0)

        def values(self):
            return self.getTypedRuleContext(IOParser.ValuesContext,0)


        def RBRACE(self):
            return self.getToken(IOParser.RBRACE, 0)

        def LBRACK(self):
            return self.getToken(IOParser.LBRACK, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def RBRACK(self):
            return self.getToken(IOParser.RBRACK, 0)

        def SEMICOL(self):
            return self.getToken(IOParser.SEMICOL, 0)

        def getRuleIndex(self):
            return IOParser.RULE_vectors

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectors" ):
                return visitor.visitVectors(self)
            else:
                return visitor.visitChildren(self)




    def vectors(self):

        localctx = IOParser.VectorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vectors)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(IOParser.LBRACE)
            self.state = 126
            self.values()
            self.state = 127
            self.match(IOParser.RBRACE)
            self.state = 128
            self.match(IOParser.LBRACK)
            self.state = 129
            self.arithExpr(0)
            self.state = 130
            self.match(IOParser.RBRACK)
            self.state = 131
            self.match(IOParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(IOParser.VarTypeContext,0)


        def IDENT(self):
            return self.getToken(IOParser.IDENT, 0)

        def LBRACK(self):
            return self.getToken(IOParser.LBRACK, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def RBRACK(self):
            return self.getToken(IOParser.RBRACK, 0)

        def SEMICOL(self):
            return self.getToken(IOParser.SEMICOL, 0)

        def getRuleIndex(self):
            return IOParser.RULE_vector

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVector" ):
                return visitor.visitVector(self)
            else:
                return visitor.visitChildren(self)




    def vector(self):

        localctx = IOParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.varType()
            self.state = 134
            self.match(IOParser.IDENT)
            self.state = 135
            self.match(IOParser.LBRACK)
            self.state = 136
            self.arithExpr(0)
            self.state = 137
            self.match(IOParser.RBRACK)
            self.state = 138
            self.match(IOParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(IOParser.VarTypeContext,0)


        def IDENT(self):
            return self.getToken(IOParser.IDENT, 0)

        def LBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.LBRACK)
            else:
                return self.getToken(IOParser.LBRACK, i)

        def arithExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.ArithExprContext)
            else:
                return self.getTypedRuleContext(IOParser.ArithExprContext,i)


        def RBRACK(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.RBRACK)
            else:
                return self.getToken(IOParser.RBRACK, i)

        def SEMICOL(self):
            return self.getToken(IOParser.SEMICOL, 0)

        def getRuleIndex(self):
            return IOParser.RULE_matrix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix" ):
                return visitor.visitMatrix(self)
            else:
                return visitor.visitChildren(self)




    def matrix(self):

        localctx = IOParser.MatrixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.varType()
            self.state = 141
            self.match(IOParser.IDENT)
            self.state = 142
            self.match(IOParser.LBRACK)
            self.state = 143
            self.arithExpr(0)
            self.state = 144
            self.match(IOParser.RBRACK)
            self.state = 145
            self.match(IOParser.LBRACK)
            self.state = 146
            self.arithExpr(0)
            self.state = 147
            self.match(IOParser.RBRACK)
            self.state = 148
            self.match(IOParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(IOParser.INT, 0)

        def LONG(self):
            return self.getToken(IOParser.LONG, 0)

        def DOUBLE(self):
            return self.getToken(IOParser.DOUBLE, 0)

        def CHAR(self):
            return self.getToken(IOParser.CHAR, 0)

        def STRING(self):
            return self.getToken(IOParser.STRING, 0)

        def getRuleIndex(self):
            return IOParser.RULE_varType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarType" ):
                return visitor.visitVarType(self)
            else:
                return visitor.visitChildren(self)




    def varType(self):

        localctx = IOParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IOParser.INT) | (1 << IOParser.LONG) | (1 << IOParser.DOUBLE) | (1 << IOParser.CHAR) | (1 << IOParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addend(self):
            return self.getTypedRuleContext(IOParser.AddendContext,0)


        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def PLUS(self):
            return self.getToken(IOParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(IOParser.MINUS, 0)

        def getRuleIndex(self):
            return IOParser.RULE_arithExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr" ):
                return visitor.visitArithExpr(self)
            else:
                return visitor.visitChildren(self)



    def arithExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IOParser.ArithExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_arithExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.addend(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 155
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 156
                    _la = self._input.LA(1)
                    if not(_la==IOParser.PLUS or _la==IOParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 157
                    self.addend(0) 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddendContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(IOParser.TermContext,0)


        def addend(self):
            return self.getTypedRuleContext(IOParser.AddendContext,0)


        def MULT(self):
            return self.getToken(IOParser.MULT, 0)

        def DIV(self):
            return self.getToken(IOParser.DIV, 0)

        def getRuleIndex(self):
            return IOParser.RULE_addend

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddend" ):
                return visitor.visitAddend(self)
            else:
                return visitor.visitChildren(self)



    def addend(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IOParser.AddendContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_addend, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.AddendContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addend)
                    self.state = 166
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 167
                    _la = self._input.LA(1)
                    if not(_la==IOParser.MULT or _la==IOParser.DIV):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 168
                    self.term() 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(IOParser.IDENT, 0)

        def NUM(self):
            return self.getToken(IOParser.NUM, 0)

        def LPAREN(self):
            return self.getToken(IOParser.LPAREN, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def RPAREN(self):
            return self.getToken(IOParser.RPAREN, 0)

        def getRuleIndex(self):
            return IOParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = IOParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_term)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOParser.IDENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(IOParser.IDENT)
                pass
            elif token in [IOParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.match(IOParser.NUM)
                pass
            elif token in [IOParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.match(IOParser.LPAREN)
                self.state = 177
                self.arithExpr(0)
                self.state = 178
                self.match(IOParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.arithExpr_sempred
        self._predicates[12] = self.addend_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithExpr_sempred(self, localctx:ArithExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def addend_sempred(self, localctx:AddendContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




