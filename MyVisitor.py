__author__ = 'Antoine MILESI, Florian Bodrero'

from data import *
from Memory import Memory
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

    def visitRealisatorPhrase(self, ctx:PhraseParser.PhraseContext):
        if ctx.STRING():
            searchValue=ctx.STRING().getText().replace("\"", "")
        else:
            raise ValueError("Missing value")
        results = self.findFilmsByValue('titre', searchValue, 'réalisateur')
        print('Le réalisateur du film ' + searchValue + ' est ' + results[0])

    def visitMovieRealPhrase(self, ctx:PhraseParser.PhraseContext):
        if ctx.STRING():
            searchValue=ctx.STRING().getText().replace("\"", "")
        else:
            raise ValueError("Missing value")
        results = self.findFilmsByValue('réalisateur', searchValue, 'titre')
        print('\n'+searchValue +' a réalisé les films suivants:')
        for value in results:
            print(str(value))

    def visitCountActorPhrase(self, ctx:PhraseParser.PhraseContext):
        if ctx.STRING():
            searchValue=ctx.STRING().getText().replace("\"", "")
        else:
            raise ValueError("Missing value")

        results = self.findFilmsByValue('acteur', searchValue, 'titre')
        print(searchValue + ' a joué dans ' + str(len(results)) + ' films.')

    def visitWhichFilmsPhrase(self, ctx:PhraseParser.PhraseContext):
        if Memory.films:
            for film in Memory.films:
                print(film['titre'])

    def visitWhichDatePhrase(self, ctx:PhraseParser.PhraseContext):
        if Memory.films:
            for film in Memory.films:
                print(film['année'])

    def visitWhichRealisatorPhrase(self, ctx:PhraseParser.PhraseContext):
        if Memory.films:
            for film in Memory.films:
                print(film['réalisateur'])


    def findFilmsByValue(self, searchKey, searchValue, wantedValue):
        Memory.films = []
        results = []
        for film in films:
            if searchKey in film:
                if film[searchKey]==searchValue:
                    Memory.films.append(film)
                    results.append(film[wantedValue])

        return results
