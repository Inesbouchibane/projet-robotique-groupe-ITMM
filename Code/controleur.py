from environnement import Environnement

class Controleur:
    def __init__(self, vitesse_gauche, vitesse_droite, mode):
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.mode = mode
        self.env = Environnement(self.vitesse_gauche, self.vitesse_droite, self.mode)
    
    def demarrer_simulation(self):
        self.env.boucle_principale()
    
    def ajuster_vitesse(self, vitesse_gauche, vitesse_droite):
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.env.robot.vitesse_gauche = vitesse_gauche
        self.env.robot.vitesse_droite = vitesse_droite
