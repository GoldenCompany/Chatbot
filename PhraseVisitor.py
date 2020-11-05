# Generated from Phrase.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PhraseParser import PhraseParser
else:
    from PhraseParser import PhraseParser

# This class defines a complete generic visitor for a parse tree produced by PhraseParser.

class PhraseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PhraseParser#énoncé.
    def visitÉnoncé(self, ctx:PhraseParser.ÉnoncéContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PhraseParser#InterpretePhrase.
    def visitInterpretePhrase(self, ctx:PhraseParser.InterpretePhraseContext):
        return self.visitChildren(ctx)



del PhraseParser