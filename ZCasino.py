# -*-coding:Latin-1 -*

import os
from random import randrange
from math import ceil

continuer_partie = True  # variable qui détermine quand la partie s' arrêtera

# Sélection du solde de départ
solde = -1
while solde <= 0:
    solde = input("Quelle est votre solde de départ? ")
    try:
        solde = int(solde)
    except ValueError:
        print("Vous n'avez pas saisi de solde.")
        solde = -1
        continue
    if solde < 1:
        print("Vous ne pouvez pas démarrer avec un solde négatif.")
print("Vous commencez la partie avec", solde, "$.")


while continuer_partie:  # Le bloc s'exécute tant que la variable est true

    # Selection du numéro
    nb = -1
    while nb < 0 or nb > 49:
        nb = input("Choisissez un numéro compris de 0 à 49 :")
        try:
            nb = int(nb)
        except ValueError:
            print("Vous n'avez pas saisi de numéro.")
            nb = -1
            continue
        if nb < 0:
            print("Vous avez saisi un numéro négatif.")
            nb = -1
        if nb > 49:
            print("Vous avez saisi un numéro supérieur à 49.")
            nb = -1

    # Selection de la mise
    mise = -1
    while mise <= 0 or mise > solde:
        mise = input("Combien misez-vous? ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas misé.")
            mise = -1
            continue
        if mise <= 0:
            print("Vous avez saisi une mise négative.")
            mise = -1
        if mise > solde:
            print("Vous avez", solde, "$. Vous ne pouvez pas miser plus.")

    # Tirage et résultat
    nb_tire = randrange(50)
    print("Le numéro tiré au hasard est le", nb_tire)
    if nb == nb_tire:
        print("Les deux numéros sont identiques. Vous gagnez", 3 * mise, "$!")
        solde += 3 * mise
    elif (nb % 2 == 0 and nb_tire % 2 == 0) or (nb % 2 == 1 and nb_tire % 2 == 1):
        print("Les deux numéros sont de la même couleur. Vous gagnez", ceil(0.5 * mise), "$!")
        solde += ceil(0.5 * mise)
    else:
        print("Perdu! Les deux numéros sont différents et n'ont pas la même couleur.")
        solde -= mise

    # Condition d'arrêt de partie
    if solde <= 0:
        print("Votre solde est de 0, veuillez rejouer une prochaine fois.")
        continuer_partie = False
    else:
        print("Vous avez ", solde, "$.")
        quitter = input("Souhaitez-vous continuer de jouer? (o/n)")
        quitter = quitter.lower()
        if quitter == "n":
            print("Vous quittez la partie avec", solde, "$. A la prochaine fois!")
            continuer_partie = False


os.system("pause")
