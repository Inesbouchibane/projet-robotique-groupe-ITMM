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
     
    def verifier_limite_carre(self):
        """
        Vérifie si le robot a parcouru la distance correspondant à un côté du carré.
        Si oui, on tourne à 90 degrés pour continuer le tracé du carré.
        """
        if self.distance_parcourue >= self.longueur_cote:
            self.distance_parcourue = 0
            self.etape_carre += 1
            if self.etape_carre < 4:
                # Tourner à 90 degrés
                self.robot.vitesse_gauche = -2
                self.robot.vitesse_droite = 2
            else:
                # Le carré est terminé
                self.strategie = None
                self.etape_carre = 0
                self.robot.en_mouvement = False