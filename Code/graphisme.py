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
#-----------------------------------mouna -----------------------------------------------------------------------------------------
class Robot:

#----------------------------------ines------------------------------------------------------------------------------------------
    def deplacer(self):

#---------------------------------------------------------------------------------------------------------------------------
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

class Environnement:
    def __init__(self, vitesse_gauche, vitesse_droite):

#-----------------------------------meriem-----------------------------------------------------------------------------------------
    def dessiner_obstacles(self): 

#------------------------takoua----------------------------------------------------------------------------------------------------
    def detecter_collision(self, x, y):

#-------------------------------------------------inesssssssssssssssssssssssssssss--meriem-------------------------------------------------------------------------
    def boucle_principale(self):

        #----------------------------------------------------------------------------------------------------------------------------

    def dessiner_trajectoire(self): # mohamed et mouna 
         #----------------------------------------------------------------------------------------------------------------------------

