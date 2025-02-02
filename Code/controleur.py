from graphisme import Environnement

class Controleur:
    def __init__(self, vitesse_gauche, vitesse_droite):
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.env = Environnement(self.vitesse_gauche, self.vitesse_droite)

    def demarrer_simulation(self):
        self.env.boucle_principale()

    def ajuster_vitesse(self, vitesse_gauche, vitesse_droite):
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.env.robot.vitesse_gauche = vitesse_gauche
        self.env.robot.vitesse_droite = vitesse_droite
<<<<<<< HEAD

=======
   
   def reinitialiser(self):
        self.env.reinitialiser_robot()
>>>>>>> 9f44f048a194d4b108ccf7f7774a639f597d8327
