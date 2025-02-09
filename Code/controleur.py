from graphisme import Environnement

class Controleur:
    def __init__(self, vitesse_gauche, vitesse_droite, mode):
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        # Le mode est soit "manuel" soit "automatique"
        self.env = Environnement(self.vitesse_gauche, self.vitesse_droite, mode)

    def demarrer_simulation(self):
        self.env.boucle_principale()

    def ajuster_vitesse(self, vitesse_gauche, vitesse_droite):
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.env.robot.vitesse_gauche = vitesse_gauche
        self.env.robot.vitesse_droite = vitesse_droite
    
    def verifier_limite_carre(self, x, y, cote):
        """ Vérifie si le carré reste dans les limites de la fenêtre. """
        if (x - cote < 0 or x + cote > self.environnement.largeur_fenetre or
            y - cote < 0 or y + cote > self.environnement.hauteur_fenetre):
            return False
        return True