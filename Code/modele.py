import pygame
import math

# Dimensions de la fenêtre
LARGEUR = 800
HAUTEUR = 600

# Couleurs
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
    
class Environnement:
    def __init__(self, vitesse_gauche, vitesse_droite):
        self.robot = Robot(LARGEUR / 2, HAUTEUR / 2, vitesse_gauche, vitesse_droite)
        self.obstacles = [pygame.Rect(200, 200, 100, 100), pygame.Rect(400, 100, 50, 50)]

    def detecter_collision(self, x, y):
        robot_rect = pygame.Rect(x - self.robot.largeur, y - self.robot.longueur, self.robot.largeur * 2, self.robot.longueur * 2)
        for obstacle in self.obstacles:
            if robot_rect.colliderect(obstacle):
                return True
        return False
