from modele import Environnement
from graphisme import Graphics

if __name__ == "__main__":
    vitesse_gauche = float(input("Entrez la vitesse de la roue gauche : "))
    vitesse_droite = float(input("Entrez la vitesse de la roue droite : "))

    env = Environnement(vitesse_gauche, vitesse_droite)
    graphics = Graphics(env)
    graphics.boucle_principale()
