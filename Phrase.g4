grammar Phrase;
enonce: (phrase NEWLINE);
phrase:
PRON_INT 'est' ARTICLE CLEF 'de' ARTICLE CLEF VALEUR '?' # InterpretePhrase
| PRON_INT 'a réalisé' VALEUR '?' # InterpretePhrase1
	;
PRON_INT: 'Quel'|'Quelle'|'Qui' ;
ARTICLE: 'le' | 'la' | 'l' ;
CLEF:
	  'titre'
	| 'annee'
	| 'acteur'
	| 'realisateur'
	| 'serie'
	;
VALEUR:  [0-9a-zA-Z]+ ;
NEWLINE: [\r\n]+ ;
WS  :   [' \t]+ -> skip ; // élimine les espaces et les '
