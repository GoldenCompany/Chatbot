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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\31\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\3\2\2\4\2")
        buf.write("\4\2\2\2\27\2\6\3\2\2\2\4\26\3\2\2\2\6\7\5\4\3\2\7\b\7")
        buf.write("\13\2\2\b\3\3\2\2\2\t\n\7\7\2\2\n\13\7\3\2\2\13\f\7\b")
        buf.write("\2\2\f\r\7\t\2\2\r\16\7\4\2\2\16\17\7\b\2\2\17\20\7\t")
        buf.write("\2\2\20\21\7\n\2\2\21\27\7\5\2\2\22\23\7\7\2\2\23\24\7")
        buf.write("\6\2\2\24\25\7\n\2\2\25\27\7\5\2\2\26\t\3\2\2\2\26\22")
        buf.write("\3\2\2\2\27\5\3\2\2\2\3\26")
        return buf.getvalue()


class PhraseParser ( Parser ):

    grammarFileName = "Phrase.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'est'", "'de'", "'?'", "'a r\u00E9alis\u00E9'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "PRON_INT", "ARTICLE", "CLEF", "VALEUR", 
                      "NEWLINE", "WS" ]

    RULE_énoncé = 0
    RULE_phrase = 1

    ruleNames =  [ "énoncé", "phrase" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    PRON_INT=5
    ARTICLE=6
    CLEF=7
    VALEUR=8
    NEWLINE=9
    WS=10

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

        def getRuleIndex(self):
            return PhraseParser.RULE_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhrase" ):
                listener.enterPhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhrase" ):
                listener.exitPhrase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhrase" ):
                return visitor.visitPhrase(self)
            else:
                return visitor.visitChildren(self)




    def phrase(self):

        localctx = PhraseParser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_phrase)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
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
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(PhraseParser.PRON_INT)
                self.state = 17
                self.match(PhraseParser.T__3)
                self.state = 18
                self.match(PhraseParser.VALEUR)
                self.state = 19
                self.match(PhraseParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





