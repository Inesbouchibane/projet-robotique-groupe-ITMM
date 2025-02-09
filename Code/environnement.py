from robot import Robot
from affichage import Affichage
import pygame
import math
import random

IR_MAX_DISTANCE = 100
IR_SEUIL_ARRET = 50
LARGEUR, HAUTEUR = 800, 600

class Environnement:
    def __init__(self, vitesse_gauche, vitesse_droite, mode):
        self.robot = Robot(LARGEUR / 2, HAUTEUR / 2, vitesse_gauche, vitesse_droite)
        self.mode = mode
        self.avoidance_mode = False
        self.avoidance_direction = None
        self.obstacles = [(200, 200, 100, 100), (400, 100, 50,
50)]
        self.affichage = Affichage(LARGEUR, HAUTEUR, self.obstacles)
    def detecter_collision(self, x, y):
        for ox, oy, ow, oh in self.obstacles:
            if ox < x < ox + ow and oy < y < oy + oh:
                return True
        return False

