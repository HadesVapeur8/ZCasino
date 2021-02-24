# Liste des imports
import Fonctions

# variable qui détermine quand la partie s' arrêtera
continuer_partie = True
# Détermination du solde de départ
solde = Fonctions.solde_depart()

while continuer_partie:
    # Saisies de l'utilisateur
    nb = Fonctions.entrer_numero()
    mise = Fonctions.entrer_mise(solde)

    # Tirage et résultat
    solde = Fonctions.tirage(nb, solde, mise)

    # Condition pour continuer la partie
    continuer_partie = Fonctions.arret_partie(solde, continuer_partie)

