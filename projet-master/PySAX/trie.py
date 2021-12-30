import time
from plot_word_extractor import words
import re

class TrieNode:
    def __init__(self, char):
        # le caractère dans le noeud
        self.char = char
        # si on est à la fin du mot
        self.is_end = False
        # le dictionnaire des fils du noeud : (clé,valeurs)=(caractère, noeuds)
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        # on vérifie l'éxistance de chaque caractère du mot dans notre Trie
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # si on trouve pas le caractère,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # marquer la fin d'un mot
        node.is_end = True

    def Traverse(self, node, prefix):
        """Parcours le Trie et contruire tous les mots commençant par le prefixe e paramètre"""
        if node.is_end:
            self.output.append((prefix + node.char))
        for child in node.children.values():
            self.Traverse(child, prefix + node.char)

    def Found(self, x):
        """cette fonction prend le "prefixe" en paramètre"""
        """trouve tous les mots du Trie commençants par ce prefixe"""
        """et affiche ces mots et le nombre de fois qu'on l'a inséré"""
        self.output = []
        node = self.root
        # vérifier si le prefixe éxiste dans le Trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        #à partir de la dernière lettre du préfixe on parcourt le Trie
        #et on renvoit tous les mots commençant par ce prefixe
        self.Traverse(node, x[:-1])

        # afficher la liste des mots triée par ordre alphabétique
        return sorted(self.output, key=lambda x: x[0])

    def sizeTrie(self, node, somme):
        """Calcule la taille d'un Trie"""
        if node.children.values() is None:
            return 0
        for child in node.children.values():
            somme = somme + 1
            somme= self.sizeTrie(child, somme)
        return somme

    def recherche0(self, node, variable):
        """Permet de rechercher un motif dans le trie à partir d'une expression régulière saisie"""
        tdebut = time.time()
        # on récupère la première ligne du trie
        premiere_ligne = []
        for child in node.children.values():
            premiere_ligne.append(child.char)

        # on récupère tout le trie
        trie = []
        for char in premiere_ligne:
            trie.append(self.Found(char))
        trie_final = []
        for sequence in trie:
            for i in range(len(sequence)):
                trie_final.append(sequence[i])
        trie = trie_final
        # on fait la recherche dans le trie
        reg = variable
        r1 = re.compile(reg)
        liste = ''
        resultat_recherche = []
        # on parcours le tri, on compare avec l'expression régulière, et on retourne le résultat de la recherche
        for sequence in trie:
            p = re.match(r1, sequence[0])
            if (p != None):
                if (p.group(0) != ''):
                    liste+=(sequence[0])
                    for i in range(len(sequence[1])):
                        liste+=(sequence[1][i])
                    resultat_recherche.append(liste)
                    liste = ''
        print("Le temps consacré à la recherche du motif : ", time.time() - tdebut)
        return (resultat_recherche)
"""-----------------------------------------------programme principal--------------------------------------------------"""
if __name__ == "__main__":

    tdebut=time.time()
    t = Trie()
    node = t.root
    for x in words:
        t.insert(x)

    tinject=time.time()-tdebut
    print("Le temps consacré à l'injection des données est de ",tinject)
    print("la taille du trié est:", t.sizeTrie(t.root, 0), "Noeuds")

    variable=input("Donner le motif recherché:\n")
    if(variable[0]=='^'):
        tdebut = time.time()
        x=t.Found("a")
        print("Le temps consacré à la recherche du motif est : ", time.time() - tdebut)
        print("le resultat de la recherche est: ", x)
        print("le nombre de résultats trouvés est: ", len(x))
    else:
        x=t.recherche0(node,variable)
        print("le resultat de la recherche est: ",x)
        print("le nombre de résultats trouvés est: ",len(x))