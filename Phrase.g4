grammar Phrase;
énoncé: (phrase NEWLINE);
phrase:
PRON_INT 'est' ARTICLE CLEF 'de' ARTICLE CLEF VALEUR '?' # KeyValuePhrase
| PRON_INT 'sont les films sortis en' YEAR '?' # DatePhrase
| PRON_INT 'films sont sortis en' YEAR '?' # DatePhrase
| PRON_INT 'a réalisé' VALEUR '?' # RealisatorPhrase
| 'Dans combien de films' STRING 'a-t-' PRON_PERS 'joué ?' # CountActorPhrase
	;
PRON_INT: 'Quel'|'Quelle'|'Quels'|'Quelles'|'Qui' ;
PRON_PERS: 'il'|'elle' ;
ARTICLE: 'le' | 'la' | 'l' ;
CLEF:
	  'titre'
	| 'année'
	| 'acteur'
	| 'réalisateur'
	| 'série'
	;
YEAR: [0-9]+ ;
VALEUR:  [0-9a-zA-Z]+ ;
STRING:
	  SINGLE_STRING
	| DOUBLE_STRING
    ;

SINGLE_STRING
    : '\'' ~('\'')+ '\''
    ;

DOUBLE_STRING
    : '"' ~('"')+ '"'
    ;

NEWLINE: [\r\n]+ ;
WS  :   (' '|'\t'|'-')+ -> skip ; // élimine les espaces et les '
