from controleur import Controleur

def main():
    vitesse_gauche = float(input("Entrez la vitesse de la roue gauche : "))
    vitesse_droite = float(input("Entrez la vitesse de la roue droite : "))
    
    controleur = Controleur(vitesse_gauche, vitesse_droite)
    controleur.demarrer_simulation()

if __name__ == "__main__":
    main()
