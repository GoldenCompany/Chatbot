__author__ = 'Pierre Jourlin'

from data import *
from PhraseVisitor import PhraseVisitor
from PhraseParser import PhraseParser


class MyVisitor(PhraseVisitor):
    def __init__(self):
        pass

    def visitÉnoncé(self, ctx:PhraseParser.ÉnoncéContext):
        return self.visitChildren(ctx)

    def visitPhrase(self, ctx:PhraseParser.PhraseContext):
        print (ctx.VALEUR())

        if ctx.CLEF(0) and ctx.CLEF(1) and ctx.VALEUR():
            wantedValue=ctx.CLEF(0).getText()
            searchKey=ctx.CLEF(1).getText()
            searchValue=ctx.VALEUR().getText()
        else:
            raise ValueError("Missing value")

        for film in films:
            if searchKey in film:
                if film[searchKey]==searchValue:
                    print(film[wantedValue])
