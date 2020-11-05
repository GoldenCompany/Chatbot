# Generated from Phrase.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5)\n")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7R\n\7\3\b\6\bU\n\b\r\b\16\bV\3\t\6\tZ\n\t\r\t\16\t")
        buf.write("[\3\n\6\n_\n\n\r\n\16\n`\3\n\3\n\2\2\13\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\3\2\5\5\2\62;C\\c|\4\2\f\f")
        buf.write("\17\17\5\2\13\13\"\"))\2m\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\31\3\2\2")
        buf.write("\2\7\34\3\2\2\2\t(\3\2\2\2\13/\3\2\2\2\rQ\3\2\2\2\17T")
        buf.write("\3\2\2\2\21Y\3\2\2\2\23^\3\2\2\2\25\26\7g\2\2\26\27\7")
        buf.write("u\2\2\27\30\7v\2\2\30\4\3\2\2\2\31\32\7f\2\2\32\33\7g")
        buf.write("\2\2\33\6\3\2\2\2\34\35\7A\2\2\35\b\3\2\2\2\36\37\7S\2")
        buf.write("\2\37 \7w\2\2 !\7g\2\2!)\7n\2\2\"#\7S\2\2#$\7w\2\2$%\7")
        buf.write("g\2\2%&\7n\2\2&\'\7n\2\2\')\7g\2\2(\36\3\2\2\2(\"\3\2")
        buf.write("\2\2)\n\3\2\2\2*+\7n\2\2+\60\7g\2\2,-\7n\2\2-\60\7c\2")
        buf.write("\2.\60\7n\2\2/*\3\2\2\2/,\3\2\2\2/.\3\2\2\2\60\f\3\2\2")
        buf.write("\2\61\62\7v\2\2\62\63\7k\2\2\63\64\7v\2\2\64\65\7t\2\2")
        buf.write("\65R\7g\2\2\66\67\7c\2\2\678\7p\2\289\7p\2\29:\7\u00eb")
        buf.write("\2\2:R\7g\2\2;<\7c\2\2<=\7e\2\2=>\7v\2\2>?\7g\2\2?@\7")
        buf.write("w\2\2@R\7t\2\2AB\7t\2\2BC\7\u00eb\2\2CD\7c\2\2DE\7n\2")
        buf.write("\2EF\7k\2\2FG\7u\2\2GH\7c\2\2HI\7v\2\2IJ\7g\2\2JK\7w\2")
        buf.write("\2KR\7t\2\2LM\7u\2\2MN\7\u00eb\2\2NO\7t\2\2OP\7k\2\2P")
        buf.write("R\7g\2\2Q\61\3\2\2\2Q\66\3\2\2\2Q;\3\2\2\2QA\3\2\2\2Q")
        buf.write("L\3\2\2\2R\16\3\2\2\2SU\t\2\2\2TS\3\2\2\2UV\3\2\2\2VT")
        buf.write("\3\2\2\2VW\3\2\2\2W\20\3\2\2\2XZ\t\3\2\2YX\3\2\2\2Z[\3")
        buf.write("\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\22\3\2\2\2]_\t\4\2\2^]\3")
        buf.write("\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\n\2")
        buf.write("\2c\24\3\2\2\2\t\2(/QV[`\3\b\2\2")
        return buf.getvalue()


class PhraseLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    PRON_INT = 4
    ARTICLE = 5
    CLEF = 6
    VALEUR = 7
    NEWLINE = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'est'", "'de'", "'?'" ]

    symbolicNames = [ "<INVALID>",
            "PRON_INT", "ARTICLE", "CLEF", "VALEUR", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "PRON_INT", "ARTICLE", "CLEF", 
                  "VALEUR", "NEWLINE", "WS" ]

    grammarFileName = "Phrase.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


