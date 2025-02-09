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

    def boucle_principale(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            ir_point = self.robot.scan_infrarouge(self.obstacles, IR_MAX_DISTANCE)
            distance_ir = math.hypot(ir_point[0] - self.robot.x, ir_point[1] - self.robot.y)
            collision = self.detecter_collision(self.robot.x, self.robot.y)

            if self.mode == "automatique":
                if distance_ir < IR_SEUIL_ARRET or collision:
                    if not self.avoidance_mode:
                        self.avoidance_direction = random.choice(["left", "right"])
                        self.avoidance_mode = True
                    if self.avoidance_direction == "left":
                        self.robot.vitesse_gauche = -abs(self.robot.vitesse_gauche)
                        self.robot.vitesse_droite = abs(self.robot.vitesse_droite)
                    else:
                        self.robot.vitesse_gauche = abs(self.robot.vitesse_gauche)
                        self.robot.vitesse_droite = -abs(self.robot.vitesse_droite)
                else:
                    if self.avoidance_mode:
                        self.avoidance_mode = False
            
            self.robot.deplacer()
            self.affichage.mettre_a_jour(self.robot, ir_point, distance_ir)
            pygame.display.flip()
            pygame.time.delay(30)
