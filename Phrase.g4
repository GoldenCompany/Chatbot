grammar Phrase;
enonce: (phrase NEWLINE);
phrase:
PRON_INT 'est' ARTICLE CLEF 'de' ARTICLE CLEF VALEUR '?' # KeyValuePhrase
| 'Quels sont les films sortis en YEAR ?' # DatePhrase
| 'Quels films sont sortis en YEAR ?' # DatePhrase
| PRON_INT 'a réalisé' VALEUR '?' # RealisatorPhrase
	;
PRON_INT: 'Quel'|'Quelle'|'Quels'|'Quelles'|'Qui' ;
ARTICLE: 'le' | 'la' | 'l' ;
CLEF:
	  'titre'
	| 'annee'
	| 'acteur'
	| 'realisateur'
	| 'serie'
	;
YEAR: [0-9]+ ;
VALEUR:  [0-9a-zA-Z]+ ;
NEWLINE: [\r\n]+ ;
WS  :   [' \t]+ -> skip ; // élimine les espaces et les '
