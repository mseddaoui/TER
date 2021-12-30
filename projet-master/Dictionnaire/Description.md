# Description:
- trie.py : un programme python de construction du trié qui contient deux classes: TrieNode represente le noeud et Trie auquel on injecte(inserer) des données "dictionnaire.txt" selon une structure arborescente, qui nous a permet d'implémenter une recherche d'un préfixe dans notre trié.
on a également mesuré la taille de notre trié en octets.
- dictionnaire.txt: notre jeu de données, mots de la langue française.
- recherche_sequentielle.sh: script bash permettant de chercher un motif de manière séquentielle sur les données stockées dans le fichier "dictionnaire.txt" tout en mesurant le temps, une combinaison entre bash pour l'expression régulière et python pour utiliser la librairie "time".
# Résultats:
- Les mots qui partagent le même préfixe partagent les mêmes noeuds par exemple: abats et abattage contiennent 4 noeuds en communs ce qui est un gain de mémoire considérable.
- Le programme retourne la liste de tous les mots qui contiennent le même préfixe.
- La taille du trié est mesuré selon le nombre de noeuds stockés dans notre structure.
