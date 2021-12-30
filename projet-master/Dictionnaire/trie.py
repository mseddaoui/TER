import time

class TrieNode:
    def __init__(self, char):
        # le caractère dans le noeud
        self.char = char
        # si on est à la fin du mot
        self.is_end = False
        # le dictionnaire des fils du noeud : (clé,valeurs)=(caractère, noeuds)
        self.children = {}

class Trie(object):
    """ l'objet 'Trie' """
    def __init__(self):
        """initialisation de notre Trie"""
        self.root = TrieNode("")

    def insert(self, word):
        """inserer un mot dans le Trie"""
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

"""-----------------------------------------------programme principal--------------------------------------------------"""
if __name__ == "__main__":

    tdebut=time.time()

    print(tdebut)
    t = Trie()
    file = open("dictionnaire.txt", "r")
    for ligne in file:
        t.insert(ligne.strip())

    tinject=time.time()-tdebut
    print("Le temps consacré à l'injection des données est de ",tinject)
    print("la taille du trié est:", t.sizeTrie(t.root, 0), "Noeuds")

    #print("\nLes mots commençant par \"abat\" sont:\n",t.Found("abat"))
    #print("\nLes mots commençant par 'a' sont:\n",t.Found("a"))
    print("\nLes mots commençant par 'p' sont:\n",t.Found("u"))
    trecherche=time.time() - tdebut
    print("Le temps consacré à la recherche du motif est de ",trecherche)
