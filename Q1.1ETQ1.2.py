# Équipe 13
# Nikolas Lévesque (20276665) et Abdelmouhcine Messaad (2151011)

import random as rnd
import numpy as np
from collections import Counter

################################################################################
#                                  Question 1.1                                #
################################################################################

# racine cubique entière
def integer_cube_root(x):
    low, high = 0, x
    while low <= high:
        mid = (low + high) // 2
        m3 = mid ** 3
        if m3 == x:
            return mid
        elif m3 < x:
            low = mid + 1
        else:
            high = mid - 1
    return high

# trouver M
C = 1101510739796100601351050380607502904616643795400781908795311659278941419415375
M = integer_cube_root(C)

# convertit M en message clair
def int_to_str(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big').decode('utf-8')

message_clair = int_to_str(M)
print(message_clair)

################################################################################
#                                  Question 1.2                                #
################################################################################

n = 172219604291138178634924980176652297603347655313304280071646410523864939208855547078498922947475940487766894695848119416017067844129458299713889703424997977808694983717968420001033168722360067307143390485095229367172423195469582545920975539060699530956357494837243598213416944408434967474317474605697904676813343577310719430442085422937057220239881971046349315235043163226355302567726074269720408051461805113819456513196492192727498270702594217800502904761235711809203123842506621973488494670663483187137290546241477681096402483981619592515049062514180404818608764516997842633077157249806627735448350463
e = 173
C = 25782248377669919648522417068734999301629843637773352461224686415010617355125387994732992745416621651531340476546870510355165303752005023118034265203513423674356501046415839977013701924329378846764632894673783199644549307465659236628983151796254371046814548224159604302737470578495440769408253954186605567492864292071545926487199114612586510433943420051864924177673243381681206265372333749354089535394870714730204499162577825526329944896454450322256563485123081116679246715959621569603725379746870623049834475932535184196208270713675357873579469122917915887954980541308199688932248258654715380981800909

# liste d'auteurs célèbres
auteurs = [
    "Guy de Maupassant", "Molière", "Émile Zola", "Albert Camus", "Victor Hugo",
    "Agatha Christie", "Stefan Zweig", "Antoine de Saint-Exupéry", "Voltaire",
    "Honoré de Balzac", "William Shakespeare", "George Orwell", "Jules Verne",
    "Jean-Paul Sartre", "Charles Baudelaire", "Jean Anouilh", "Boris Vian",
    "Eugène Ionesco", "J.R.R. Tolkien", "Gustave Flaubert", "Robert Louis Stevenson",
    "Romain Gary", "Albert Cohen", "Pierre de Marivaux", "Jean Racine",
    "Georges Simenon", "Alexandre Dumas", "Franz Kafka", "Jean Giono", "Primo Levi",
    "Prosper Mérimée", "Jack London", "John Steinbeck", "René Barjavel",
    "Isaac Asimov", "Marguerite Duras", "Jane Austen", "Marcel Proust",
    "Françoise Sagan", "La Fontaine", "Pierre Corneille", "Denis Diderot",
    "Louis-Ferdinand Céline", "Alfred de Musset", "Arthur Conan Doyle",
    "Marcel Pagnol", "Fiodor Dostoïevski", "Oscar Wilde", "Beaumarchais", "Stendhal"
]

# convertit string en entier avec l'encodage UTF-8)
def str_to_int(x):
    return int.from_bytes(x.encode('utf-8'), byteorder='big')

# parcourir la liste des auteurs pour trouver le message clair
for auteur in auteurs:
    M = str_to_int(auteur)
    nom_chiffre = pow(M, e, n)
    if nom_chiffre == C:
        print(auteur)
        break