import pygame
import math
from modele import LARGEUR, HAUTEUR, BLEU, ROUGE, VERT

NOIR = (0,0,0)

class Graphics:
   def __init__(self, environnement):
        self.ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("Simulation de Robot")
        self.clock = pygame.time.Clock()
        self.env = environnement
        self.trajectoire=[]
        
   def dessiner_obstacles(self):
        for obstacle in self.env.obstacles:
            pygame.draw.rect(self.ecran, ROUGE, obstacle)


   def dessiner_robot(self):
        robot = self.env.robot
        angle_rad = math.radians(robot.angle)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)

        points = [
            (robot.x + cos_a * robot.longueur / 2 - sin_a * robot.largeur / 2,
             robot.y - sin_a * robot.longueur / 2 - cos_a * robot.largeur / 2),
            (robot.x - cos_a * robot.longueur / 2 - sin_a * robot.largeur / 2,
             robot.y + sin_a * robot.longueur / 2 - cos_a * robot.largeur / 2),
            (robot.x - cos_a * robot.longueur / 2 + sin_a * robot.largeur / 2,
             robot.y + sin_a * robot.longueur / 2 + cos_a * robot.largeur / 2),
            (robot.x + cos_a * robot.longueur / 2 + sin_a * robot.largeur / 2,
             robot.y - sin_a * robot.longueur / 2 + cos_a * robot.largeur / 2),
        ]

        pygame.draw.polygon(self.ecran, BLEU, points)
        pointe_x = robot.x + cos_a * robot.longueur / 2
        pointe_y = robot.y - sin_a * robot.longueur / 2
        pygame.draw.line(self.ecran, VERT, (robot.x, robot.y), (pointe_x, pointe_y), 3)
   
   def dessiner_trajectoire(self):
    if len(self.trajectoire) > 1:
        pygame.draw.lines(self.ecran, NOIR, False, self.trajectoire, 2)


   def boucle_principale(self):
        from controleur import gerer_evenements

        running = True
        while running:
            running = gerer_evenements(self.env.robot)
            
            if self.env.robot.en_mouvement:
                new_x = self.env.robot.x
                new_y = self.env.robot.y
                
                dx = (self.env.robot.vitesse_gauche + self.env.robot.vitesse_droite) / 2 * math.cos(math.radians(self.env.robot.angle))
                dy = -(self.env.robot.vitesse_gauche + self.env.robot.vitesse_droite) / 2 * math.sin(math.radians(self.env.robot.angle))

                if not self.env.detecter_collision(new_x + dx, new_y + dy):
                    self.env.robot.x += dx
                    self.env.robot.y += dy
                    # Ajouter la position actuelle du robot à la trajectoire
                self.trajectoire.append((self.env.robot.x, self.env.robot.y))
         
            # Dessiner la trajectoire
            self.dessiner_trajectoire()

            self.ecran.fill((255, 255, 255))
            self.dessiner_obstacles()
            self.dessiner_robot()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

     

   def detecter_collision(self, x, y):
       robot_rect = pygame.Rect(x - self.robot.largeur, y - self.robot.longueur,self.robot.largeur * 2, self.robot.longueur * 2)
       for obstacle in self.obstacles:
           if robot_rect.colliderect(obstacle):
              return True
       return False
