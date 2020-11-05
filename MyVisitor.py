__author__ = 'Pierre Jourlin'

from PhraseVisitor import PhraseVisitor
from PhraseParser import PhraseParser


class MyVisitor(PhraseVisitor):
    def __init__(self):
        pass

    def visitÉnoncé(self, ctx):
        return self.visit(ctx.phrase())

    def visitInterpretePhrase(self, ctx):
        if ctx.CLEF(0) and ctx.CLEF(1) and ctx.VALEUR():
            valeur_demandée=ctx.CLEF(0).getText()
            clef_recherchée=ctx.CLEF(1).getText()
            valeur_recherchée=ctx.VALEUR().getText()
        else:
            raise ValueError("Missing value")

        return (valeur_demandée, clef_recherchée, valeur_recherchée)
