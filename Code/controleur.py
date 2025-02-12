from environnement import Environnement

class Controleur:
    def __init__(self, vitesse_gauche, vitesse_droite, mode):
        """
        Initialise le contrôleur avec les vitesses des roues et le mode de simulation.
        :param vitesse_gauche: Vitesse de la roue gauche.
        :param vitesse_droite: Vitesse de la roue droite.
        :param mode: Mode de simulation (automatique, manuel, carré).
        """
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.mode = mode
        self.env = Environnement(self.vitesse_gauche, self.vitesse_droite, self.mode)
    
    def demarrer_simulation(self):
        """
        Démarre la simulation en fonction du mode choisi.
        """
        self.env.boucle_principale()
    
    def ajuster_vitesse(self, vitesse_gauche, vitesse_droite):
        """
        Ajuste les vitesses des roues du robot.
        :param vitesse_gauche: Nouvelle vitesse de la roue gauche.
        :param vitesse_droite: Nouvelle vitesse de la roue droite.
        """
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.env.robot.vitesse_gauche = vitesse_gauche
        self.env.robot.vitesse_droite = vitesse_droite

