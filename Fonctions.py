# -*-coding:Latin-1 -*

# Liste des modules
from random import randrange
from math import ceil


def solde_depart():
    """D�termine la solde de d�part.

    La fonction continue tant que la somme entr�e est invalide"""
    solde = -1
    while solde <= 0:  # La solde est demand� tant que celle-ci est invalide
        solde = input("Quelle est votre solde de d�part? ")
        try:
            solde = int(solde)
        except ValueError:  # S'assure qu'une somme a �t� rentr�e
            print("Vous n'avez pas saisi de solde.")
            solde = -1
            continue
        if solde < 1:  # S'assure que le solde entr� est > 1
            print("Vous ne pouvez pas d�marrer avec un solde n�gatif.")
    print("Vous commencez la partie avec", solde, "$.")
    return solde


def entrer_numero():
    """Demande � l'utilisateur le num�ro entre 0 et 49 qu'il d�sire.

    La fonction continue tant que le num�ro entr� est invalide."""
    nb = -1
    while nb < 0 or nb > 49:  # Le num�ro est demand� tant qu'il est invalide
        nb = input("Choisissez un num�ro compris de 0 � 49 :")
        try:
            nb = int(nb)
        except ValueError:  # S'assure qu'un num�ro est entr�
            print("Vous n'avez pas saisi de num�ro.")
            nb = -1
            continue
        if nb < 0:  # S'assure que le num�ro est positif
            print("Vous avez saisi un num�ro n�gatif.")
            nb = -1
        if nb > 49:  # S'assure que le num�ro est < 49
            print("Vous avez saisi un num�ro sup�rieur � 49.")
            nb = -1
    return nb


def entrer_mise(solde):
    """Permet � l'utilisateur d'entrer la mise qu'il d�sire.

    La fonction continue tant que la mise est invalide."""
    mise = -1
    while mise <= 0 or mise > solde:  # La mise est demand� tant qu'elle est invalide
        mise = input("Combien misez-vous? ")
        try:
            mise = int(mise)
        except ValueError:  # S'assure qu'une somme est entr�
            print("Vous n'avez pas mis�.")
            mise = -1
            continue
        if mise <= 0:  # S'assure que la somme entr�e est positive
            print("Vous avez saisi une mise n�gative.")
            mise = -1
        if mise > solde:  # S'assure que la somme entr� est < solde
            print("Vous avez", solde, "$. Vous ne pouvez pas miser plus.")
    return mise


def tirage(nb, solde, mise):
    """Tire un num�ro au hasard et le compare � celui de l'utilisateur.

    Il compare les num�ros sur leur valeur et leur couleur (rouge ou noir)."""
    nb_tire = randrange(50)  # Tirage du num�ro
    print("Le num�ro tir� au hasard est le", nb_tire)
    # D�termination des gains
    if nb == nb_tire:
        print("Les deux num�ros sont identiques. Vous gagnez", 3 * mise, "$!")
        solde += 3 * mise
    elif (nb % 2 == 0 and nb_tire % 2 == 0) or (nb % 2 == 1 and nb_tire % 2 == 1):
        print("Les deux num�ros sont de la m�me couleur. Vous gagnez", ceil(0.5 * mise), "$!")
        solde += ceil(0.5 * mise)
    else:
        print("Perdu! Les deux num�ros sont diff�rents et n'ont pas la m�me couleur.")
        solde -= mise
    return solde


def arret_partie(solde, continuer_partie):
    """D�termine si la partie doit continuer ou s'arr�ter."""
    if solde <= 0:  # La partie s'arr�te si le solde <= 0
        print("Votre solde est de 0, veuillez rejouer une prochaine fois.")
        continuer_partie = False
    else:
        print("Vous avez ", solde, "$.")
        quitter = -1
        while quitter == -1:  # La question continue d'etre pos�e tant que l'a r�ponse est invalide
            quitter = input("Souhaitez-vous continuer de jouer? (o/n)")
            try:
                quitter = quitter.lower()
                assert quitter == "o" or quitter == "n"
            except AssertionError:  # S'assure que la r�ponse est "n" ou "o"
                quitter = -1
                continue
            if quitter == "n":  # La partie s'arr�te si la r�ponse est "n"
                print("Vous quittez la partie avec", solde, "$. A la prochaine fois!")
                continuer_partie = False
    return continuer_partie
