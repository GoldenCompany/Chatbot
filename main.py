#!/usr/bin/python3 main.py
# coding:utf8
# (c) Pierre Jourlin, novembre 2020

__author__ = 'Pierre Jourlin'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from data import *
from PhraseLexer import PhraseLexer
from PhraseParser import PhraseParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = PhraseLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PhraseParser(token_stream)
    tree = parser.énoncé()
    visitor = MyVisitor()
    try:
        (demande, clef_recherche, valeur_recherche)=visitor.visit(tree)
    except ValueError:
        print('Cette phrase n\'est pas valide ')
        sys.exit()

    for film in films:
        if clef_recherche in film:
            if film[clef_recherche]==valeur_recherche:
                print(film[demande])
