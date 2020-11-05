grammar Phrase;
énoncé: (phrase NEWLINE);
phrase:
PRON_INT 'est' ARTICLE CLEF 'de' ARTICLE CLEF VALEUR '?'
| PRON_INT 'a réalisé' VALEUR '?'
	;
PRON_INT: 'Quel'|'Quelle'|'Qui' ;
ARTICLE: 'le' | 'la' | 'l' ;
CLEF:
	  'titre'
	| 'année'
	| 'acteur'
	| 'réalisateur'
	| 'série'
	;
VALEUR:  [0-9a-zA-Z]+ ;
NEWLINE: [\r\n]+ ;
WS  :   [' \t]+ -> skip ; // élimine les espaces et les '
