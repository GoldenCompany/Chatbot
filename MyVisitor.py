__author__ = 'Antoine MILESI'

from data import *
from PhraseVisitor import PhraseVisitor
from PhraseParser import PhraseParser


class MyVisitor(PhraseVisitor):
    def __init__(self):
        pass

    def visitÉnoncé(self, ctx:PhraseParser.ÉnoncéContext):
        return self.visitChildren(ctx)

    def visitKeyValuePhrase(self, ctx:PhraseParser.PhraseContext):
        if ctx.CLEF(0) and ctx.CLEF(1) and ctx.VALEUR():
            wantedValue=ctx.CLEF(0).getText()
            searchKey=ctx.CLEF(1).getText()
            searchValue=ctx.VALEUR().getText()
        else:
            raise ValueError("Missing value")

        results = self.findFilmsByValue(searchKey, searchValue, wantedValue)
        for value in results:
            print(value)

    def visitDatePhrase(self, ctx:PhraseParser.PhraseContext):
        if ctx.YEAR():
            searchValue=ctx.YEAR().getText()
        else:
            raise ValueError("Missing value")

        results = self.findFilmsByValue('année', searchValue, 'titre')
        for value in results:
            print(value)

    def findFilmsByValue(self, searchKey, searchValue, wantedValue):
        results = []
        for film in films:
            if searchKey in film:
                if film[searchKey]==searchValue:
                    results.append(film[wantedValue])

        return results
