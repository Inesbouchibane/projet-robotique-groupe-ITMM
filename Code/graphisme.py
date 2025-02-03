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


    def deplacer(self):
        if not self.en_mouvement:
            return
        
        vitesse_moyenne = (self.vitesse_gauche + self.vitesse_droite) / 2
        delta_angle = (self.vitesse_droite - self.vitesse_gauche) / self.largeur * 10
        
        self.angle += delta_angle
        self.angle %= 360
        
        dx = vitesse_moyenne * math.cos(math.radians(self.angle))
        dy = -vitesse_moyenne * math.sin(math.radians(self.angle))
        
        self.x = max(self.largeur, min(LARGEUR - self.largeur, self.x + dx))
        self.y = max(self.longueur, min(HAUTEUR - self.longueur, self.y + dy))


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

#-----------------------------------meriem-----------------------------------------------------------------------------------------
    def dessiner_obstacles(self): 

#------------------------takoua----------------------------------------------------------------------------------------------------
    def detecter_collision(self, x, y):
<<<<<<< HEAD

#-------------------------------------------------inesssssssssssssssssssssssssssss--meriem-------------------------------------------------------------------------

    #meriem -----------------------------
    def reinitialiser_robot(self):
     
    
    def boucle_principale(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.robot.en_mouvement = False
                    elif event.key == pygame.K_d:
                        self.robot.vitesse_gauche = float(input("Entrez la vitesse de la roue gauche : "))
                        self.robot.vitesse_droite = float(input("Entrez la vitesse de la roue droite : "))
                        self.robot.en_mouvement = True
            
            if self.robot.en_mouvement:
                # Calcul de la nouvelle position
                new_x = self.robot.x
                new_y = self.robot.y
                vitesse_moyenne = (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2
                delta_angle = (self.robot.vitesse_droite - self.robot.vitesse_gauche) / self.robot.largeur * 10
                
                self.robot.angle += delta_angle
                self.robot.angle %= 360
                
                dx = vitesse_moyenne * math.cos(math.radians(self.robot.angle))
                dy = -vitesse_moyenne * math.sin(math.radians(self.robot.angle))
                
                if not self.detecter_collision(new_x + dx, new_y + dy):
                    self.robot.x = max(self.robot.largeur, min(LARGEUR - self.robot.largeur, new_x + dx))
                    self.robot.y = max(self.robot.longueur, min(HAUTEUR - self.robot.longueur, new_y + dy))
                    # Enregistrer la nouvelle position dans la trajectoire
                    self.trajectoire.append((self.robot.x, self.robot.y))
            
            # Mise à jour de l'affichage
            self.ecran.fill(BLANC)
            self.dessiner_obstacles()
            self.robot.dessiner(self.ecran)
            self.dessiner_trajectoire()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

        #----------------------------------------------------------------------------------------------------------------------------

    def dessiner_trajectoire(self):   
        if len(self.trajectoire) > 1:
            pygame.draw.lines(self.ecran, NOIR, False, self.trajectoire, 2)
