import numpy as np
import csv
import math
import matplotlib.pyplot as plt
import re

from scipy import stats

from trie import Trie

import time

def regression_lineaire():
    """calculer la régression linéaire (stats.linregress)"""
    """récuperer la pente de la droite de régression (pente)"""
    """récuperer l'arc tangent en radians (math.atan)"""
    """convertir les angles de radians en degrées (math.degrees) et le retourner"""
    X = np.arange(xSize)
    i = 0
    angle = []
    while i < xSize - 1:
        tmp = []
        x = X[i:i + 2]
        y = ordonnee[i:i + 2]

        pente, intercept, rvalue, pvalue, err = stats.linregress(x, y)
        alpha = math.degrees(math.atan(pente))
        tmp.append(alpha)
        tmp.append(date[i])
        tmp.append(date[i + 1])
        angle.append(tmp)
        i += 1
    return angle


def symbolisation(angle):
    """représentation des degrés de la pente entre deux dates consécutives en symboles alphabétiques"""
    """on se ramène à un groupe de 26 grace au modulo"""
    tab = []
    i = 0
    j = 3.46
    alpha_montee = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
    alpha_descente = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphamontee = []
    alphadescente = []
    while (j <= 90):
        tmp = []
        tmp.append(alpha_montee[i])
        tmp.append(j - 3.46)
        tmp.append(j)
        alphamontee.append(tmp)
        i = i + 1
        j += 3.46
    
    i = 0
    j = -3.46
    while (j >= -90):
        tmp = []
        tmp.append(alpha_descente[i])
        tmp.append(j + 3.46)
        tmp.append(j)
        alphadescente.append(tmp)
        i += 1
        j -= 3.46
    
    tmp = []
    for c in angle:
        if (c[0] >= 0):
            for d in alphamontee:
                if ((c[0] >= d[1]) & (c[0] < d[2])):
                    tmp.append(d[0])
                    tmp.append(c[1])
                    tmp.append(c[2])
                    tmp.append(c[0])
                    tab.append(tmp)
        else:
            for d in alphadescente:
                if (c[0] < d[1]) & (c[0] > d[2]):
                    tmp.append(d[0])
                    tmp.append(c[1])
                    tmp.append(c[2])
                    tmp.append(c[0])
                    tab.append(tmp)
        tmp = []
   
    return tab


def generer_sequence(tab):
    """le découpage se fait en fonction des lettres"""
    """on regroupe les miniscules et les majuscules dans des sous-séquences """
    """exemple :une lettre miniscule suivi d'une lettre majuscules représente 2 sous-séquences différentes"""

    mots = []
    i = 0
    numeroSeq = 0
    while i < len(tab):
        alph = ''
        date = ''
        mot = []
        debut = True
        # sous-séquences de lettres miniscules
        while (ord(tab[i][0]) >= ord('a') and ord(tab[i][0]) <= ord('z')):
            if debut:
                alph = tab[i][0]
                date = tab[i][1]
                debut = False
            else:
                alph = alph + tab[i][0]

            if (i < len(tab) - 1):
                i += 1
            else:
                mot.append(alph)
                mot.append(date)
                mot.append(tab[i][2])
                mot.append(numeroSeq)
                mots.append(mot)
                return mots
                # changement de sous-séquences
        if not debut:
            mot.append(alph)
            mot.append(date)
            mot.append(tab[i - 1][2])
            mot.append(numeroSeq)
            mots.append(mot)
            numeroSeq += 1
        debut = True
        alph = ''
        date = ''
        mot = []
        # sous-séquences de lettres majuscules
        while (ord(tab[i][0]) >= ord('A') and ord(tab[i][0]) <= ord('Z')):
            if debut:
                alph = tab[i][0]
                date = tab[i][1]
                debut = False
            else:
                alph = alph + tab[i][0]
            if (i < len(tab) - 1):
                i += 1
            else:
                mot.append(alph)
                mot.append(date)
                mot.append(tab[i][2])
                mot.append(numeroSeq)
                mots.append(mot)
                return mots
        # changement de sous-séquences
        if not debut:
            mot.append(alph)
            mot.append(date)
            mot.append(tab[i - 1][2])
            mot.append(numeroSeq)
            mots.append(mot)
            numeroSeq += 1

    return mots


def creation_trie(data):
    """Permet de créer notre Trié à partir des données du fichier """
    t = Trie()
    for sequence in data:
        information = []
        information.append(sequence[1])
        information.append(sequence[2])
        information.append(sequence[3])
        t.insert(sequence[0], information)
    return t

def tracer_courbe(angle, ordonnee):
    """permettant l'affichage de notre courbe"""
    x = []
    y = []
    x.append(angle[1][1])

    for s in angle:
        x.append(s[2])
    for i in ordonnee:
        y.append(i)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, color='tab:blue')
    plt.show()


def recherche(t, variable, angle, ordonnee):
    """Permet de faire la recherche dans le trie à partir de l'expression régulière"""
    """Puis affiche le résultat en rouge dans le graphe initial, et aussi sous forme d'une liste"""

    temps=time.time()
    # Créer la figure de notre courbe initiale en bleu
    x = []
    y = []
    x.append(angle[0][1])

    for s in angle:
        x.append(s[2])
    for i in ordonnee:
        y.append(i)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, y, color='tab:blue')

    # La recherche du motif saisi
    if(variable[0]!='^'):
        node = t.root
        liste=t.recherche0(node,variable)
        liste=sorted(liste, key=lambda sequence: sequence[2])

        print("!!!!! le temps consacré à la recherche du motif", time.time()-temps)
        print("Le résultat de notre recherche est:", liste)
        print("sa longeur=",len(liste))
    else:
        liste=t.Found(variable[1])
        print("!!!!! le temps consacré à la recherche du motif2", time.time()-temps)
        print("les résultat de votre recherche est:", liste)

    # Pour afficher ce resultat en rouge dans notre tracé:
    # D'abord on récupère toutes les intervales
    xrouge = []
    for k in liste:
        xrouge.append(k[1])
        xrouge.append(k[2])
    # Ensuite on récupère les indices de chaque date appartenant à ces intervales
    indices = []
    indices1 = []
    indices2 = []
    j = 0
    for a in xrouge:
        while (j <= (len(x))):
            if (a == str(x[j])):
                indices.append(j + 1)
                j = j + 1
                break
            else:
                j += 1
    for i in range(len(indices)):
        if (i % 2 == 0):
            indices1.append(indices[i])
        else:
            indices2.append(indices[i])
    # Enfin on transorme ces couples de dates en des couples de leurs indices
    o = []
    indices3 = []
    for i in range(len(indices1)):
        indices3.append(indices1[i])
        indices3.append(indices2[i])
        o.append(indices3)
        indices3 = []

    # Puis on affiche Notre résultat en rouge sur notre tracé initial
    for i in o:
        ax.plot(x[int(i[0] - 1):int(i[1])], y[int(i[0] - 1):int(i[1])], color='tab:red')
    plt.show()


if __name__ == "__main__":
    """ d'abord on récupére les données du fichier sous forme de deux listes (date[] et ordonnee[])"""
    date = []
    ordonnee = []
    xSize = 0
    file = open("CAC40.csv", "r")
    #file = open("export_meteo_versailles_2015_2020.csv", "r")
    try:
        reader = csv.reader(file)
        for row in reader:
            tmp = []
            date.append(row[0])
            ordonnee.append(float((row[1])))
            xSize += 1
    finally:
        file.close()

    tdebut=time.time()

    angle = regression_lineaire()#on calcule les angles
    tregression=time.time() -tdebut
    print("!!!!!! le temps de la régression est", tregression)

    tab = symbolisation(angle)#on transforme en lettre chaque intervalle d'un jour, par rapport à sa regression linéaire
    #print("\n+++++++++++++++++ résultat de la symbolisation Pente:+++++++++++++++++\n", tab)
    tsymbol=time.time() - tdebut
    print("!!!!!!!! le temps de la symbolisation est",tsymbol)

    """aprés la symbolisation on peut afficher le mot qui représente notre courbe comme suit"""
    mot = ''
    for row in tab:
        for i in row:
            mot += (row[0])
    #print("\nLa courbe sous forme d'un mot= ", mot)

    data = generer_sequence(tab)#on découpe not mot en sous séquences tout en récupérant leurs intervales de temps
    #print("\n++++++++++++++ résultat de découpage en Sous-Séquences :++++++++++++++\n", data)
    tgenerer=time.time()-tdebut
    print("!!!!!!!! le temps de la generation de sequences est",tgenerer)

    """On crée le trier à partir de ces sous séquences"""
    t = Trie()
    t=creation_trie(data)
    tcreation=time.time()-tdebut
    print("!!!!!!!! le temps consacré pour la creation du trie est",tcreation)
    
    #tracer_courbe(angle, ordonnee)#on trace notre courbe initial
    
    variable = input("\nDonner le motif recherché:\n----------------------------------------------------------------------------\n|'^[A]*'--> ce qui commene par A\n|'(AZ)*' --> ensemble\n| '(A)$' --> A tout seul\n|'[A-Z]*'--> toutes les majuscules\n"
        "|'[a-z]*'--> toutes les minuscules\n"
        )

    recherche(t, variable, angle, ordonnee)#on fait la recherche dans notre Trié à partir de l'éxpression régulière saisie
    