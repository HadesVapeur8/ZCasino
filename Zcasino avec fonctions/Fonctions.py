# -*-coding:Latin-1 -*

# Liste des modules
from random import randrange
from math import ceil


def solde_depart():
    """Détermine la solde de départ.

    La fonction continue tant que la somme entrée est invalide"""
    solde = -1
    while solde <= 0:  # La solde est demandé tant que celle-ci est invalide
        solde = input("Quelle est votre solde de départ? ")
        try:
            solde = int(solde)
        except ValueError:  # S'assure qu'une somme a été rentrée
            print("Vous n'avez pas saisi de solde.")
            solde = -1
            continue
        if solde < 1:  # S'assure que le solde entré est > 1
            print("Vous ne pouvez pas démarrer avec un solde négatif.")
    print("Vous commencez la partie avec", solde, "$.")
    return solde


def entrer_numero():
    """Demande à l'utilisateur le numéro entre 0 et 49 qu'il désire.

    La fonction continue tant que le numéro entré est invalide."""
    nb = -1
    while nb < 0 or nb > 49:  # Le numéro est demandé tant qu'il est invalide
        nb = input("Choisissez un numéro compris de 0 à 49 :")
        try:
            nb = int(nb)
        except ValueError:  # S'assure qu'un numéro est entré
            print("Vous n'avez pas saisi de numéro.")
            nb = -1
            continue
        if nb < 0:  # S'assure que le numéro est positif
            print("Vous avez saisi un numéro négatif.")
            nb = -1
        if nb > 49:  # S'assure que le numéro est < 49
            print("Vous avez saisi un numéro supérieur à 49.")
            nb = -1
    return nb


def entrer_mise(solde):
    """Permet à l'utilisateur d'entrer la mise qu'il désire.

    La fonction continue tant que la mise est invalide."""
    mise = -1
    while mise <= 0 or mise > solde:  # La mise est demandé tant qu'elle est invalide
        mise = input("Combien misez-vous? ")
        try:
            mise = int(mise)
        except ValueError:  # S'assure qu'une somme est entré
            print("Vous n'avez pas misé.")
            mise = -1
            continue
        if mise <= 0: # S'assure que la somme entrée est positive
            print("Vous avez saisi une mise négative.")
            mise = -1
        if mise > solde:  # S'assure que la somme entré est < solde
            print("Vous avez", solde, "$. Vous ne pouvez pas miser plus.")
    return mise


def tirage(nb, solde, mise):
    """Tire un numéro au hasard et le compare à celui de l'utilisateur.

    Il compare les numéros sur leur valeur et leur couleur (rouge ou noir)."""
    nb_tire = randrange(50)  # Tirage du numéro
    print("Le numéro tiré au hasard est le", nb_tire)
    # Détermination des gains
    if nb == nb_tire:
        print("Les deux numéros sont identiques. Vous gagnez", 3 * mise, "$!")
        solde += 3 * mise
    elif (nb % 2 == 0 and nb_tire % 2 == 0) or (nb % 2 == 1 and nb_tire % 2 == 1):
        print("Les deux numéros sont de la même couleur. Vous gagnez", ceil(0.5 * mise), "$!")
        solde += ceil(0.5 * mise)
    else:
        print("Perdu! Les deux numéros sont différents et n'ont pas la même couleur.")
        solde -= mise
    return solde


def arret_partie(solde, continuer_partie):
    """Détermine si la partie doit continuer ou s'arrêter."""
    if solde <= 0:  # La partie s'arrête si le solde <= 0
        print("Votre solde est de 0, veuillez rejouer une prochaine fois.")
        continuer_partie = False
    else:
        print("Vous avez ", solde, "$.")
        quitter = -1
        while quitter == -1:  # La question continue d'etre posée tant que l'a réponse est invalide
            quitter = input("Souhaitez-vous continuer de jouer? (o/n)")
            try:
                quitter = quitter.lower()
                assert quitter == "o" or quitter == "n"
            except AssertionError:  # S'assure que la réponse est "n" ou "o"
                quitter = -1
                continue
            if quitter == "n":  # La partie s'arrête si la réponse est "n"
                print("Vous quittez la partie avec", solde, "$. A la prochaine fois!")
                continuer_partie = False
    return continuer_partie
