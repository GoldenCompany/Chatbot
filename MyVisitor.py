__author__ = 'Pierre Jourlin'

from PhraseVisitor import PhraseVisitor
from PhraseParser import PhraseParser


class MyVisitor(PhraseVisitor):
    def __init__(self):
        pass 
           
    def visitÉnoncé(self, ctx):
        return self.visit(ctx.phrase())

    def visitInterpretePhrase(self, ctx):
        valeur_demandée=ctx.CLEF(0).getText()
        clef_recherchée=ctx.CLEF(1).getText()
        valeur_recherchée=ctx.VALEUR().getText()
        return (valeur_demandée, clef_recherchée, valeur_recherchée)



