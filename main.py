#!/usr/bin/python3 main.py
# coding:utf8

__author__ = 'Florian Bodrero'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from PhraseLexer import PhraseLexer
from PhraseParser import PhraseParser
from MyVisitor import MyVisitor

if __name__ == '__main__':
    while True:
        print("Taper une question ou exit ou Ctrl+C pour fermer cette fenêtre")
        if len(sys.argv) > 1:
            input_stream = FileStream(sys.argv[1])
        else:
            input_stream = InputStream(sys.stdin.readline())

        if str(input_stream).replace("\n", "") == "exit":
            sys.exit()

        lexer = PhraseLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PhraseParser(token_stream)
        tree = parser.énoncé()
        visitor = MyVisitor()
        try:
            visitor.visit(tree)
        except ValueError:
            print('Cette phrase n\'est pas valide.')
            sys.exit()
