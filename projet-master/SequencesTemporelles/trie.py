import re
import time
class TrieNode:
    def __init__(self, char, information):
        # information contenue dans la feuille
        self.information = []

        # le caractère dans le noeud
        self.char = char

        # si on est à la fin du mot
        self.is_end = False

        # le dictionnaire des fils du noeud : (clé,valeurs)=(caractère, noeuds)
        self.children = {}

class Trie(object):
    """ l'objet 'Trie' """

    def __init__(self):
        """
        initialisation de notre Trie
        """
        self.root = TrieNode("*", [0, 0])

    def insert(self, word, information):
        """inserer un mot dans le Trie"""
        node = self.root
        # on vérifie l'éxistance de chaque caractère du mot dans notre arbre
        for char in word:
            if (char in node.children):
                node = node.children[char]
            else:
                # si on trouve pas le caractère,
                # On crée un nouveau noeud dans le trie
                new_node = TrieNode(char, information)
                node.children[char] = new_node
                node = new_node
        node.information.append(information)
        # marquer la fin d'un mot
        node.is_end = True

    def Traverse(self, node, prefix):
        """Parcours le Trie et contruit tous les mots commençant par le prefixe e paramètre"""
        liste = []
        if node.is_end:
            for i in range(len(node.information)):
                liste.append(prefix + node.char)
                liste.append(node.information[i])
                self.output.append(liste)
                liste = []
        for child in node.children.values():
            self.Traverse(child, prefix + node.char)
        
        return self.output

    def Found(self, x):
        """cette fonction prend le "prefixe" en paramètre,et trouve tous les mots
        du Trie commençants par ce prefixe, et affiche ces mots et le nombre de fois qu'on l'a inséré
        """
        temps=time.time()

        self.output = []
        node = self.root
        # vérifier si le prefixe éxiste dans le Trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        # parcourir le Trie à partir du dernier noeud du préfixe
        # pour trouver tous les mots commençant par ce prefixe
        self.Traverse(node, x[:-1])
      
        return (self.output)

    def sizeTrie(self, node, somme):
        """Méthode permettant de calculer la taille d'un trié"""
        if node.children.values() is None:
            return 0
        for child in node.children.values():
            somme = somme + 1
            somme = self.sizeTrie(child, somme)
        return somme

    def recherche0(self, node, variable):
        """Permet de rechercher un motif dans le trie à partir d'une expression régulière saisie"""
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
        liste = []
        resultat_recherche = []
        # on parcours le tri, on compare avec l'expression régulière, et on retourne le résultat de la recherche
        for sequence in trie:
            p = re.match(r1, sequence[0])
            if (p != None):
                if (p.group(0) != ''):
                    liste.append(sequence[0])
                    for i in range(len(sequence[1])):
                        liste.append(sequence[1][i])
                    resultat_recherche.append(liste)
                    liste = []

        return (resultat_recherche)

"""-------------------------------------------------programme principal------------------------------------------------"""
if __name__ == "__main__":
    t = Trie()
    node = t.root
    t.insert("hackathon", ["12/10/1996", "20/10/1996"])
    t.insert("hackathon", ["10/10/1996", "18/10/1996"])
    t.insert("bonjour", ["10/10/1996", "18/10/1996"])
    t.insert("Bonjour", ["01/10/1996", "02/10/1996"])
    print("la taille du trié est ", t.sizeTrie(t.root, 0), "octets")
    variable = input("****Veuillez donner le motif de votre recherche sous forme d'une expression régulière:\n")
    recherche = t.recherche0(node, variable)
    print("Le résultat de votre recherche: ", recherche)