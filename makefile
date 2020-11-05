all: PhraseLexer.py
clean: 
	rm Phrase.interp PhraseLexer.* PhraseParser.* PhraseVisitor.* *.tokens
PhraseLexer.py:	Phrase.g4
	antlr4 -visitor -no-listener -Dlanguage=Python3 Phrase.g4
