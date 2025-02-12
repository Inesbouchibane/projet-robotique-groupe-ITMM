from controleur import Controleur

def main():
    """
    Fonction principale pour démarrer la simulation.
    """
    vitesse_gauche = float(input("Entrez la vitesse de la roue gauche : "))
    vitesse_droite = float(input("Entrez la vitesse de la roue droite : "))

    mode = ""
    while mode.lower() not in ["a", "m", "c"]:
        mode = input("Choisissez le mode : automatique (a), manuel (m) ou carré (c) ? ")
    
    if mode.lower() == "a":
        mode_str = "automatique"
    elif mode.lower() == "m":
        mode_str = "manuel"
    else:
        mode_str = "carré"

    controleur = Controleur(vitesse_gauche, vitesse_droite, mode_str)
    controleur.demarrer_simulation()

if __name__ == "__main__":
    main()
