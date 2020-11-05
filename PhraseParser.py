# Generated from Phrase.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\24\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2\21\2\6\3\2\2\2")
        buf.write("\4\t\3\2\2\2\6\7\5\4\3\2\7\b\7\n\2\2\b\3\3\2\2\2\t\n\7")
        buf.write("\6\2\2\n\13\7\3\2\2\13\f\7\7\2\2\f\r\7\b\2\2\r\16\7\4")
        buf.write("\2\2\16\17\7\7\2\2\17\20\7\b\2\2\20\21\7\t\2\2\21\22\7")
        buf.write("\5\2\2\22\5\3\2\2\2\2")
        return buf.getvalue()


class PhraseParser ( Parser ):

    grammarFileName = "Phrase.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'est'", "'de'", "'?'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PRON_INT", "ARTICLE", "CLEF", "VALEUR", "NEWLINE", 
                      "WS" ]

    RULE_énoncé = 0
    RULE_phrase = 1

    ruleNames =  [ "énoncé", "phrase" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    PRON_INT=4
    ARTICLE=5
    CLEF=6
    VALEUR=7
    NEWLINE=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ÉnoncéContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def phrase(self):
            return self.getTypedRuleContext(PhraseParser.PhraseContext,0)


        def NEWLINE(self):
            return self.getToken(PhraseParser.NEWLINE, 0)

        def getRuleIndex(self):
            return PhraseParser.RULE_énoncé

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterÉnoncé" ):
                listener.enterÉnoncé(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitÉnoncé" ):
                listener.exitÉnoncé(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitÉnoncé" ):
                return visitor.visitÉnoncé(self)
            else:
                return visitor.visitChildren(self)




    def énoncé(self):

        localctx = PhraseParser.ÉnoncéContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_énoncé)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.phrase()
            self.state = 5
            self.match(PhraseParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhraseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PhraseParser.RULE_phrase

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InterpretePhraseContext(PhraseContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PhraseParser.PhraseContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRON_INT(self):
            return self.getToken(PhraseParser.PRON_INT, 0)
        def ARTICLE(self, i:int=None):
            if i is None:
                return self.getTokens(PhraseParser.ARTICLE)
            else:
                return self.getToken(PhraseParser.ARTICLE, i)
        def CLEF(self, i:int=None):
            if i is None:
                return self.getTokens(PhraseParser.CLEF)
            else:
                return self.getToken(PhraseParser.CLEF, i)
        def VALEUR(self):
            return self.getToken(PhraseParser.VALEUR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpretePhrase" ):
                listener.enterInterpretePhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpretePhrase" ):
                listener.exitInterpretePhrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterpretePhrase" ):
                return visitor.visitInterpretePhrase(self)
            else:
                return visitor.visitChildren(self)



    def phrase(self):

        localctx = PhraseParser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_phrase)
        try:
            localctx = PhraseParser.InterpretePhraseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(PhraseParser.PRON_INT)
            self.state = 8
            self.match(PhraseParser.T__0)
            self.state = 9
            self.match(PhraseParser.ARTICLE)
            self.state = 10
            self.match(PhraseParser.CLEF)
            self.state = 11
            self.match(PhraseParser.T__1)
            self.state = 12
            self.match(PhraseParser.ARTICLE)
            self.state = 13
            self.match(PhraseParser.CLEF)
            self.state = 14
            self.match(PhraseParser.VALEUR)
            self.state = 15
            self.match(PhraseParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





