# Description:
- CAC40.csv: données de bourse en fonction des dates.
- export_meteo_versailles_2015_2020.csv: température en fontion de la date.
- courbe.py: programme python qui consiste à utiliser les jeux de données "CAC40.csv" ou "export_meteo_versailles_2015_2020.csv" de manière à calculer l'angle de la régression linéaire, représenter ces degrés entre deux dates consécutives en symboles alphabétiques, ce qui permet de générer des sous-séquences de lettres majuscules ou miniscules, ces dernières sont injectées dans notre trié grâce à "trie.py", dans le but d'implémenter un moteur de recherche de motifs en utilisant des expressions régulières sur notre trié, pour illustrer cela on a décidé de représenter le résultat sous forme d'une courbe représentative.
- trie.py: un programme python permettant de construire un Trie où on peut enregistrer nos sous-séquences tout en sauvgardant leurs intervalles de temps dans les feuilles.
- intervalle_lettre.txt: fichier contenant deux listes qui correspondent respectivement à l'intervalle(en degré) de chaque lettre majuscule et miniscule.

# Résultats:
Ce programme nous permet de trouver efficacement des sous-séquences temporelles suivant un motif donné dans notre trié tel que:
- Le motif est donné en entrée sur la console sous forme d'une expression régulière.
- Les lettres miniscules/ majuscules correspond à un intervalle descendants/montants de la courbe.
- La courbe initiale est de couleur bleu tandis que le résultat du motif recherché est de couleur rouge.
