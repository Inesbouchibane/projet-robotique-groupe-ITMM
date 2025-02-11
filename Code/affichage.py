import pygame
import math

BLANC, NOIR, BLEU, ROUGE, VERT, CYAN, MAGENTA = (255,255,255), (0,0,0), (0,0,255), (255,0,0), (0,255,0), (0,255,255), (255,0,255)

class Affichage:
    def __init__(self, largeur, hauteur, obstacles):
        pygame.init()
        self.ecran = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Simulation Robot")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 30)
        self.obstacles = obstacles
        self.trajet = []  
def mettre_a_jour(self, robot, ir_point, distance_ir):
        self.ecran.fill(BLANC)
        self.trajet.append((robot.x, robot.y))
        if len(self.trajet) > 1:
            pygame.draw.lines(self.ecran, NOIR, False, self.trajet, 2)
