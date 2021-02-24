# Liste des imports
import Fonctions
from tkinter import *
from tkinter.ttk import Combobox


# Création de l'interface
fenetre_principale = Tk()
fenetre = Tk()

# Création de la fenetre d'entrée
Label(fenetre_principale, text="Bienvenu dans ZCasino! \n Veuillez entrer le solde de départ : ").grid(row=0)
solde = Entry(fenetre_principale, width=10)
solde.grid(row=0, column=1, pady=10)

# Création des labels

# Création des listes de saisies de de leur positionnement


# Création des boutons
Button(fenetre, text="quitter le casino", command=fenetre.quit).grid(
    row=3, column=0, sticky=W, pady=10)

fenetre.mainloop()
