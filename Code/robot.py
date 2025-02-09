import math

class Robot:
    def __init__(self, x, y, vitesse_gauche, vitesse_droite):
        self.x, self.y = x, y
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.angle = 0
        self.largeur, self.longueur = 20, 40


