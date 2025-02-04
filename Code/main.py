from controleur import Controleur

def main():
    try:
        vitesse_gauche = float(input("Entrez la vitesse de la roue gauche : "))
        vitesse_droite = float(input("Entrez la vitesse de la roue droite : "))
    except ValueError:
        print("Veuillez entrer des valeurs numériques valides.")
        return

    mode = ""
    while mode.lower() not in ["a", "m"]:
        mode = input("Choisissez le mode : automatique (a) ou manuel (m) ? ")
    mode_str = "automatique" if mode.lower() == "a" else "manuel"

    controleur = Controleur(vitesse_gauche, vitesse_droite, mode_str)
    controleur.demarrer_simulation()

if __name__ == "__main__":
    main()
