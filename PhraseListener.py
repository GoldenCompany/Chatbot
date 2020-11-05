# Generated from Phrase.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PhraseParser import PhraseParser
else:
    from PhraseParser import PhraseParser

# This class defines a complete listener for a parse tree produced by PhraseParser.
class PhraseListener(ParseTreeListener):

    # Enter a parse tree produced by PhraseParser#énoncé.
    def enterÉnoncé(self, ctx:PhraseParser.ÉnoncéContext):
        pass

    # Exit a parse tree produced by PhraseParser#énoncé.
    def exitÉnoncé(self, ctx:PhraseParser.ÉnoncéContext):
        pass


    # Enter a parse tree produced by PhraseParser#phrase.
    def enterPhrase(self, ctx:PhraseParser.PhraseContext):
        pass

    # Exit a parse tree produced by PhraseParser#phrase.
    def exitPhrase(self, ctx:PhraseParser.PhraseContext):
        pass



del PhraseParser