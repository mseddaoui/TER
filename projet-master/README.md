## Représentaion de Séries Temporelles Symboliques par un Trié:

Ce projet rentre dans le cadre de l'UE TER(traveaux encadrés de recherche) et qui consiste à représenter une séquence temporelle avec une structure arborescente "trié" afin de pourvoir retrouver des motifs.

# Fichiers:
### Dictionnaire : 
* trie.py: un programme python de construction du trié (contenant).
* dictionnaire.txt: dictionnaire de la langue française, données injectées dans le trié(contenu) 
### PySAX :
* Comporte un programme Python utilisant la librairie SAX ainsi que le fichier CAC40.csv . 
### SéquencesTemporelles : 
* courbe.py: programme python qui consiste à manipuler des différentes données de sorte à calculer la régression linéaire, symboliser l'angle issu de cette derniere afin de générer des séquences qu'on utilise pour rechercher des motifs à l'aide des expréssions régulières, ce travail est illustré par une courbe représentative.
* recherche_sequentielle.sh: script bash permettant de chercher un motif de manière séquentielle sur les données stockées dans un fichier tout en mesurant le temps. 
* CAC40.csv: actions de bourse, une série temporelle utilisée.
* export_meteo_versailles_2015_2020.csv: degré de température de la ville de Versailles, deuxième jeu de données utilisées.
* intervalle_lettre.txt: fichier contenant deux listes qui correspondent respectivement à l'intervalle(en degré) de chaque lettre majuscule et miniscule.


# Utilisation:
1. trie.py : modifiez le main selon le préfixe que vous cherchez dans notre structure pour avoir tous les mots qui commencent par ce préfixe.
2. courbe.py: les affichages (print) de la symbolisation et de la  génération de séquences.
3. La recherche du motif se fait en utilisant les expréssions régulières définies ci-dessous, tapées sur la console:
- '^[A]* '--> ce qui commence par A ou une autre lettre.
- '(A)$'  --> A tout seul, uniquement une seule lettre.
- '(AZ)*' --> un ensemble de deux lettre | '(A...Z)*' un ensemble de n lettres avec n<=26.
- '[A-D]*'--> ensemble de lettre entre A et D incluse(A,B,C,D).
- '[A-Z]*'--> toutes les lettres majuscules.
cette recherche permet de visualiser les différents angles des lettres ou de l'ensemble de lettres grace à la représentation sur la courbe.

# Remarques importantes:
* La recherche peut ne pas aboutir pour certaines lettres comme 'o' et ça s'explique au fait que notre jeu de données ne permet pas d'avoir l'angle qui correspond à cette lettre.
* La recherche peut se faire en utilisant des lettres majuscules(comme vu ci-dessus) tout comme les lettres miniscules.
* Les lettres majuscules signifient un intervalle montant de la courbe.
* Les lettres miniscules signifient un intervalle descendant de la courbe.
* Pour vérification: l'expression '[a-zA-Z]*' permet de colorer en rouge toute la courbe.
 


