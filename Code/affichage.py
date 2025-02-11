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
