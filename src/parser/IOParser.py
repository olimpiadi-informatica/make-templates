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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("\u009f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\2\5\2&\n\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\6\3/\n\3\r\3\16\3\60\3\3")
        buf.write("\7\3\64\n\3\f\3\16\3\67\13\3\3\4\3\4\3\4\3\4\6\4=\n\4")
        buf.write("\r\4\16\4>\5\4A\n\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5I\n\5\3")
        buf.write("\6\6\6L\n\6\r\6\16\6M\3\6\3\6\3\7\3\7\5\7T\n\7\3\b\3\b")
        buf.write("\3\b\6\bY\n\b\r\b\16\bZ\3\t\3\t\3\t\3\t\7\ta\n\t\f\t\16")
        buf.write("\td\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0087")
        buf.write("\n\16\f\16\16\16\u008a\13\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u0092\n\17\f\17\16\17\u0095\13\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\5\20\u009d\n\20\3\20\2\4\32\34\21")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\6\4\2\36\36")
        buf.write("  \3\2\3\7\3\2\b\t\3\2\n\f\2\u009f\2%\3\2\2\2\4*\3\2\2")
        buf.write("\2\68\3\2\2\2\bH\3\2\2\2\nK\3\2\2\2\fS\3\2\2\2\16X\3\2")
        buf.write("\2\2\20\\\3\2\2\2\22e\3\2\2\2\24m\3\2\2\2\26t\3\2\2\2")
        buf.write("\30~\3\2\2\2\32\u0080\3\2\2\2\34\u008b\3\2\2\2\36\u009c")
        buf.write("\3\2\2\2 !\7\27\2\2!\"\7 \2\2\"#\7\30\2\2#$\7 \2\2$&\7")
        buf.write("\24\2\2% \3\2\2\2%&\3\2\2\2&\'\3\2\2\2\'(\5\4\3\2()\5")
        buf.write("\6\4\2)\3\3\2\2\2*+\7\31\2\2+,\7\24\2\2,\65\5\b\5\2-/")
        buf.write("\7\26\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61\62\3\2\2\2\62\64\5\b\5\2\63.\3\2\2\2\64\67\3\2")
        buf.write("\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\5\3\2\2\2\67\65\3")
        buf.write("\2\2\289\7\32\2\29@\7\24\2\2:<\5\n\6\2;=\7\26\2\2<;\3")
        buf.write("\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@:\3\2\2")
        buf.write("\2@A\3\2\2\2AB\3\2\2\2BC\5\f\7\2C\7\3\2\2\2DI\5\16\b\2")
        buf.write("EI\5\22\n\2FI\5\24\13\2GI\5\26\f\2HD\3\2\2\2HE\3\2\2\2")
        buf.write("HF\3\2\2\2HG\3\2\2\2I\t\3\2\2\2JL\t\2\2\2KJ\3\2\2\2LM")
        buf.write("\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\25\2\2P\13")
        buf.write("\3\2\2\2QT\5\16\b\2RT\5\24\13\2SQ\3\2\2\2SR\3\2\2\2T\r")
        buf.write("\3\2\2\2UV\5\20\t\2VW\7\25\2\2WY\3\2\2\2XU\3\2\2\2YZ\3")
        buf.write("\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\17\3\2\2\2\\]\5\30\r\2]b\7")
        buf.write(" \2\2^_\7\23\2\2_a\7 \2\2`^\3\2\2\2ad\3\2\2\2b`\3\2\2")
        buf.write("\2bc\3\2\2\2c\21\3\2\2\2db\3\2\2\2ef\7\21\2\2fg\5\16\b")
        buf.write("\2gh\7\22\2\2hi\7\17\2\2ij\5\32\16\2jk\7\20\2\2kl\7\25")
        buf.write("\2\2l\23\3\2\2\2mn\5\30\r\2no\7\17\2\2op\5\32\16\2pq\7")
        buf.write("\20\2\2qr\7 \2\2rs\7\25\2\2s\25\3\2\2\2tu\5\30\r\2uv\7")
        buf.write("\17\2\2vw\5\32\16\2wx\7\20\2\2xy\7\17\2\2yz\5\32\16\2")
        buf.write("z{\7\20\2\2{|\7 \2\2|}\7\25\2\2}\27\3\2\2\2~\177\t\3\2")
        buf.write("\2\177\31\3\2\2\2\u0080\u0081\b\16\1\2\u0081\u0082\5\34")
        buf.write("\17\2\u0082\u0088\3\2\2\2\u0083\u0084\f\3\2\2\u0084\u0085")
        buf.write("\t\4\2\2\u0085\u0087\5\34\17\2\u0086\u0083\3\2\2\2\u0087")
        buf.write("\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\33\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c\b\17")
        buf.write("\1\2\u008c\u008d\5\36\20\2\u008d\u0093\3\2\2\2\u008e\u008f")
        buf.write("\f\3\2\2\u008f\u0090\t\5\2\2\u0090\u0092\5\36\20\2\u0091")
        buf.write("\u008e\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\35\3\2\2\2\u0095\u0093\3\2")
        buf.write("\2\2\u0096\u009d\7 \2\2\u0097\u009d\7\37\2\2\u0098\u0099")
        buf.write("\7\r\2\2\u0099\u009a\5\32\16\2\u009a\u009b\7\16\2\2\u009b")
        buf.write("\u009d\3\2\2\2\u009c\u0096\3\2\2\2\u009c\u0097\3\2\2\2")
        buf.write("\u009c\u0098\3\2\2\2\u009d\37\3\2\2\2\17%\60\65>@HMSZ")
        buf.write("b\u0088\u0093\u009c")
        return buf.getvalue()


class IOParser ( Parser ):

    grammarFileName = "IOParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'long'", "'double'", "'char'", 
                     "'string'", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'['", "']'", "'{'", "'}'", "','", "':'", "';'", 
                     "'\n'", "'repeat'", "'upto'", "'input'", "'output'" ]

    symbolicNames = [ "<INVALID>", "INT", "LONG", "DOUBLE", "CHAR", "STRING", 
                      "PLUS", "MINUS", "MULT", "DIV", "MOD", "LPAREN", "RPAREN", 
                      "LBRACK", "RBRACK", "LBRACE", "RBRACE", "COMMA", "COLON", 
                      "SEMICOL", "NL", "REPEAT", "UPTO", "INPUT", "OUTPUT", 
                      "WS", "INLINE_COMMENT", "BLOCK_COMMENT", "STR", "NUM", 
                      "IDENT" ]

    RULE_filespec = 0
    RULE_inputfile = 1
    RULE_outputfile = 2
    RULE_inputline = 3
    RULE_headerline = 4
    RULE_outputline = 5
    RULE_values = 6
    RULE_homoValues = 7
    RULE_vectors = 8
    RULE_vector = 9
    RULE_matrix = 10
    RULE_vartype = 11
    RULE_arithExpr = 12
    RULE_addend = 13
    RULE_term = 14

    ruleNames =  [ "filespec", "inputfile", "outputfile", "inputline", "headerline", 
                   "outputline", "values", "homoValues", "vectors", "vector", 
                   "matrix", "vartype", "arithExpr", "addend", "term" ]

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
    MOD=10
    LPAREN=11
    RPAREN=12
    LBRACK=13
    RBRACK=14
    LBRACE=15
    RBRACE=16
    COMMA=17
    COLON=18
    SEMICOL=19
    NL=20
    REPEAT=21
    UPTO=22
    INPUT=23
    OUTPUT=24
    WS=25
    INLINE_COMMENT=26
    BLOCK_COMMENT=27
    STR=28
    NUM=29
    IDENT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FilespecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputfile(self):
            return self.getTypedRuleContext(IOParser.InputfileContext,0)


        def outputfile(self):
            return self.getTypedRuleContext(IOParser.OutputfileContext,0)


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
            return IOParser.RULE_filespec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilespec" ):
                return visitor.visitFilespec(self)
            else:
                return visitor.visitChildren(self)




    def filespec(self):

        localctx = IOParser.FilespecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_filespec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IOParser.REPEAT:
                self.state = 30
                self.match(IOParser.REPEAT)
                self.state = 31
                self.match(IOParser.IDENT)
                self.state = 32
                self.match(IOParser.UPTO)
                self.state = 33
                self.match(IOParser.IDENT)
                self.state = 34
                self.match(IOParser.COLON)


            self.state = 37
            self.inputfile()
            self.state = 38
            self.outputfile()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputfileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(IOParser.INPUT, 0)

        def COLON(self):
            return self.getToken(IOParser.COLON, 0)

        def inputline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IOParser.InputlineContext)
            else:
                return self.getTypedRuleContext(IOParser.InputlineContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.NL)
            else:
                return self.getToken(IOParser.NL, i)

        def getRuleIndex(self):
            return IOParser.RULE_inputfile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputfile" ):
                return visitor.visitInputfile(self)
            else:
                return visitor.visitChildren(self)




    def inputfile(self):

        localctx = IOParser.InputfileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_inputfile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(IOParser.INPUT)
            self.state = 41
            self.match(IOParser.COLON)
            self.state = 42
            self.inputline()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IOParser.NL:
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 43
                    self.match(IOParser.NL)
                    self.state = 46 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==IOParser.NL):
                        break

                self.state = 48
                self.inputline()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputfileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(IOParser.OUTPUT, 0)

        def COLON(self):
            return self.getToken(IOParser.COLON, 0)

        def outputline(self):
            return self.getTypedRuleContext(IOParser.OutputlineContext,0)


        def headerline(self):
            return self.getTypedRuleContext(IOParser.HeaderlineContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.NL)
            else:
                return self.getToken(IOParser.NL, i)

        def getRuleIndex(self):
            return IOParser.RULE_outputfile

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputfile" ):
                return visitor.visitOutputfile(self)
            else:
                return visitor.visitChildren(self)




    def outputfile(self):

        localctx = IOParser.OutputfileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_outputfile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(IOParser.OUTPUT)
            self.state = 55
            self.match(IOParser.COLON)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IOParser.STR or _la==IOParser.IDENT:
                self.state = 56
                self.headerline()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 57
                    self.match(IOParser.NL)
                    self.state = 60 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==IOParser.NL):
                        break



            self.state = 64
            self.outputline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputlineContext(ParserRuleContext):
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
            return IOParser.RULE_inputline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputline" ):
                return visitor.visitInputline(self)
            else:
                return visitor.visitChildren(self)




    def inputline(self):

        localctx = IOParser.InputlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inputline)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.values()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.vectors()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.vector()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.matrix()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOL(self):
            return self.getToken(IOParser.SEMICOL, 0)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.STR)
            else:
                return self.getToken(IOParser.STR, i)

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(IOParser.IDENT)
            else:
                return self.getToken(IOParser.IDENT, i)

        def getRuleIndex(self):
            return IOParser.RULE_headerline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeaderline" ):
                return visitor.visitHeaderline(self)
            else:
                return visitor.visitChildren(self)




    def headerline(self):

        localctx = IOParser.HeaderlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_headerline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                _la = self._input.LA(1)
                if not(_la==IOParser.STR or _la==IOParser.IDENT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IOParser.STR or _la==IOParser.IDENT):
                    break

            self.state = 77
            self.match(IOParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def values(self):
            return self.getTypedRuleContext(IOParser.ValuesContext,0)


        def vector(self):
            return self.getTypedRuleContext(IOParser.VectorContext,0)


        def getRuleIndex(self):
            return IOParser.RULE_outputline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputline" ):
                return visitor.visitOutputline(self)
            else:
                return visitor.visitChildren(self)




    def outputline(self):

        localctx = IOParser.OutputlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_outputline)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.values()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
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
        self.enterRule(localctx, 12, self.RULE_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 83
                self.homoValues()
                self.state = 84
                self.match(IOParser.SEMICOL)
                self.state = 88 
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

        def vartype(self):
            return self.getTypedRuleContext(IOParser.VartypeContext,0)


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
        self.enterRule(localctx, 14, self.RULE_homoValues)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.vartype()
            self.state = 91
            self.match(IOParser.IDENT)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IOParser.COMMA:
                self.state = 92
                self.match(IOParser.COMMA)
                self.state = 93
                self.match(IOParser.IDENT)
                self.state = 98
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
        self.enterRule(localctx, 16, self.RULE_vectors)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(IOParser.LBRACE)
            self.state = 100
            self.values()
            self.state = 101
            self.match(IOParser.RBRACE)
            self.state = 102
            self.match(IOParser.LBRACK)
            self.state = 103
            self.arithExpr(0)
            self.state = 104
            self.match(IOParser.RBRACK)
            self.state = 105
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

        def vartype(self):
            return self.getTypedRuleContext(IOParser.VartypeContext,0)


        def LBRACK(self):
            return self.getToken(IOParser.LBRACK, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(IOParser.ArithExprContext,0)


        def RBRACK(self):
            return self.getToken(IOParser.RBRACK, 0)

        def IDENT(self):
            return self.getToken(IOParser.IDENT, 0)

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
        self.enterRule(localctx, 18, self.RULE_vector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.vartype()
            self.state = 108
            self.match(IOParser.LBRACK)
            self.state = 109
            self.arithExpr(0)
            self.state = 110
            self.match(IOParser.RBRACK)
            self.state = 111
            self.match(IOParser.IDENT)
            self.state = 112
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

        def vartype(self):
            return self.getTypedRuleContext(IOParser.VartypeContext,0)


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

        def IDENT(self):
            return self.getToken(IOParser.IDENT, 0)

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
        self.enterRule(localctx, 20, self.RULE_matrix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.vartype()
            self.state = 115
            self.match(IOParser.LBRACK)
            self.state = 116
            self.arithExpr(0)
            self.state = 117
            self.match(IOParser.RBRACK)
            self.state = 118
            self.match(IOParser.LBRACK)
            self.state = 119
            self.arithExpr(0)
            self.state = 120
            self.match(IOParser.RBRACK)
            self.state = 121
            self.match(IOParser.IDENT)
            self.state = 122
            self.match(IOParser.SEMICOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
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
            return IOParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = IOParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_arithExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.addend(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.ArithExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                    self.state = 129
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 130
                    _la = self._input.LA(1)
                    if not(_la==IOParser.PLUS or _la==IOParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 131
                    self.addend(0) 
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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

        def MOD(self):
            return self.getToken(IOParser.MOD, 0)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_addend, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.term()
            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IOParser.AddendContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_addend)
                    self.state = 140
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 141
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IOParser.MULT) | (1 << IOParser.DIV) | (1 << IOParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 142
                    self.term() 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_term)
        try:
            self.state = 154
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IOParser.IDENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(IOParser.IDENT)
                pass
            elif token in [IOParser.NUM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(IOParser.NUM)
                pass
            elif token in [IOParser.LPAREN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(IOParser.LPAREN)
                self.state = 151
                self.arithExpr(0)
                self.state = 152
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
        self._predicates[12] = self.arithExpr_sempred
        self._predicates[13] = self.addend_sempred
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
         




