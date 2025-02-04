import pygame
import math

# Dimensions de la fenêtre
LARGEUR = 800
HAUTEUR = 600

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

class Robot:
   def __init__(self, x, y, vitesse_gauche, vitesse_droite):
        self.x = x
        self.y = y
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.angle = 0
        self.longueur = 40
        self.largeur = 20
        self.en_mouvement = True
        self.trajectoire=[]

    def dessiner(self, ecran):
 
        angle_rad = math.radians(self.angle)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)

        points = [
            (self.x + cos_a * self.longueur / 2 - sin_a * self.largeur / 2,
             self.y - sin_a * self.longueur / 2 - cos_a * self.largeur / 2),
            (self.x - cos_a * self.longueur / 2 - sin_a * self.largeur / 2,
             self.y + sin_a * self.longueur / 2 - cos_a * self.largeur / 2),
            (self.x - cos_a * self.longueur / 2 + sin_a * self.largeur / 2,
             self.y + sin_a * self.longueur / 2 + cos_a * self.largeur / 2),
            (self.x + cos_a * self.longueur / 2 + sin_a * self.largeur / 2,
             self.y - sin_a * self.longueur / 2 + cos_a * self.largeur / 2),
        ]

        pygame.draw.polygon(ecran, BLEU, points)
        # Tracer une ligne indiquant la direction (le "nez" du robot)
        pointe_x = self.x + cos_a * self.longueur / 2
        pointe_y = self.y - sin_a * self.longueur / 2
        pygame.draw.line(ecran, VERT, (self.x, self.y), (pointe_x, pointe_y), 3)
        
        
        #----------------------------------------------------------------------------------------------------------------------------

  def reinitialiser(self):
        """Remet le robot à son état initial."""
        self.x = 400  # Position initiale X
        self.y = 300  # Position initiale Y
        self.vitesse_gauche = 0 
        self.vitesse_droite = 0  
        self.angle = 0 
        self.en_mouvement = True 

class Environnement:
    def __init__(self, vitesse_gauche, vitesse_droite):
        self.ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("Simulation de Robot")
        self.clock = pygame.time.Clock()
        self.robot = Robot(LARGEUR / 2, HAUTEUR / 2, vitesse_gauche, vitesse_droite)
        self.obstacles = [pygame.Rect(200, 200, 100, 100), pygame.Rect(400, 100, 50, 50)]

#-----------------------------------meriem-----------------------------------------------------------------------------------------
    def dessiner_obstacles(self): 

#------------------------takoua----------------------------------------------------------------------------------------------------
    def detecter_collision(self, x, y):
      robot_rect = pygame.Rect(x - self.robot.largeur, y - self.robot.longueur, self.robot.largeur * 2, self.robot.longueur * 2)
        for obstacle in self.obstacles:
            if robot_rect.colliderect(obstacle):
                return True
        return False

#-------------------------------------------------inesssssssssssssssssssssssssssss--meriem-------------------------------------------------------------------------

    #meriem -----------------------------
    def reinitialiser_robot(self):
     """Réinitialise la position et la vitesse du robot."""
        self.robot.x = LARGEUR / 2
        self.robot.y = HAUTEUR / 2
        self.robot.angle = 0
        self.robot.vitesse_gauche = 0
        self.robot.vitesse_droite = 0
        self.robot.en_mouvement = False
    

        pygame.quit()

        #----------------------------------------------------------------------------------------------------------------------------

    def dessiner_trajectoire(self):   
        """ Cette fonction dessine la trah=jecetoire du robot en temps réel"""
        if len(self.trajectoire) > 1:
            pygame.draw.lines(self.ecran, NOIR, False, self.trajectoire, 2)
