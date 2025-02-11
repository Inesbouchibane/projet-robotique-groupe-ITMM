import pygame

class Affichage:
    def __init__(self, largeur, hauteur, obstacles):
        self.largeur = largeur
        self.hauteur = hauteur
        self.obstacles = obstacles
        pygame.init()
        self.ecran = pygame.display.set_mode((largeur, hauteur))
        self.font = pygame.font.Font(None, 24)  # Police pour afficher le texte