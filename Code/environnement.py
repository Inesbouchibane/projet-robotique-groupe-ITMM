
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
        """
        Initialise l'environnement de simulation.
        :param vitesse_gauche: Vitesse de la roue gauche.
        :param vitesse_droite: Vitesse de la roue droite.
        :param mode: Mode de simulation (automatique, manuel, carré).
        """
        self.robot = Robot(LARGEUR / 2, HAUTEUR / 2, vitesse_gauche, vitesse_droite)
        self.mode = mode
        self.obstacles = [(200, 200, 100, 100), (400, 100, 50, 50)]
        self.affichage = Affichage(LARGEUR, HAUTEUR, self.obstacles)
        self.avoidance_mode = False
        self.avoidance_direction = None
        self.avoidance_counter = 0
        self.default_vg = vitesse_gauche
        self.default_vd = vitesse_droite

    def detecter_collision(self, x, y):
        """
        Détecte une collision entre le robot et un obstacle.
        :param x: Position x du robot.
        :param y: Position y du robot.
        :return: True si collision, False sinon.
        """
        for ox, oy, ow, oh in self.obstacles:
            if ox < x < ox + ow and oy < y < oy + oh:
                return True
        return False

    def boucle_principale(self):
        """
        Boucle principale de la simulation.
        """
        if self.mode == "carré":
            self.dessiner_carre()
            return

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.mode == "manuel":
                        if event.key == pygame.K_s:
                            self.robot.vitesse_gauche = 0
                            self.robot.vitesse_droite = 0
                            print("Robot arrêté")
                        elif event.key == pygame.K_d:
                            try:
                                new_vg = float(input("Entrez la nouvelle vitesse de la roue gauche : "))
                                new_vd = float(input("Entrez la nouvelle vitesse de la roue droite : "))
                            except ValueError:
                                print("Valeurs invalides. Utilisation des vitesses par défaut (2).")
                                new_vg, new_vd = 2, 2
                            self.robot.vitesse_gauche = new_vg
                            self.robot.vitesse_droite = new_vd
                            self.default_vg = new_vg
                            self.default_vd = new_vd
                            print("Robot démarré avec nouvelles vitesses")
                        elif event.key == pygame.K_r:
                            self.robot.x, self.robot.y = LARGEUR / 2, HAUTEUR / 2
                            self.affichage.reset_trajet()
                            print("Robot réinitialisé")

            old_x, old_y = self.robot.x, self.robot.y
            self.robot.deplacer()
            if self.detecter_collision(self.robot.x, self.robot.y):
                self.robot.x, self.robot.y = old_x, old_y

            ir_point = self.robot.scan_infrarouge(self.obstacles, IR_MAX_DISTANCE)
            distance_ir = math.hypot(ir_point[0] - self.robot.x, ir_point[1] - self.robot.y)

            if self.mode == "automatique":
                if distance_ir < IR_SEUIL_ARRET or self.detecter_collision(self.robot.x, self.robot.y):
                    if not self.avoidance_mode:
                        self.avoidance_direction = random.choice(["left", "right"])
                        self.avoidance_mode = True
                        self.avoidance_counter = 30
                    else:
                        if self.avoidance_counter > 0:
                            self.avoidance_counter -= 1
                    if self.avoidance_direction == "left":
                        self.robot.vitesse_gauche = -abs(self.default_vg)
                        self.robot.vitesse_droite = abs(self.default_vd)
                    else:
                        self.robot.vitesse_gauche = abs(self.default_vg)
                        self.robot.vitesse_droite = -abs(self.default_vd)
                else:
                    if self.avoidance_mode and self.avoidance_counter == 0:
                        self.avoidance_mode = False
                        self.robot.vitesse_gauche = self.default_vg
                        self.robot.vitesse_droite = self.default_vd

            self.affichage.mettre_a_jour(self.robot, ir_point, distance_ir)
            pygame.display.flip()
            pygame.time.delay(30)

    def dessiner_carre(self):
        """
        Fait dessiner un carré par le robot.
        """
        SEGMENT_LENGTH = 200
        TURN_CYCLES = 30

        if not hasattr(self, 'square_initialized'):
            self.square_state = 'move'
            self.segment_travelled = 0
            self.current_segment = 0
            self.turn_cycles = 0
            self.square_initialized = True
            self.robot.vitesse_gauche = self.default_vg
            self.robot.vitesse_droite = self.default_vd
            self.segment_start_x = self.robot.x
            self.segment_start_y = self.robot.y

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            old_x, old_y = self.robot.x, self.robot.y

            if self.square_state == 'move':
                self.robot.deplacer()
                dx = self.robot.x - self.segment_start_x
                dy = self.robot.y - self.segment_start_y
                self.segment_travelled = (dx**2 + dy**2) ** 0.5
                if self.segment_travelled >= SEGMENT_LENGTH:
                    self.square_state = 'turn'
                    self.turn_cycles = TURN_CYCLES
            elif self.square_state == 'turn':
                self.robot.vitesse_gauche = -abs(self.default_vg)
                self.robot.vitesse_droite = abs(self.default_vd)
                self.robot.deplacer()
                self.turn_cycles -= 1
                if self.turn_cycles <= 0:
                    self.robot.vitesse_gauche = self.default_vg
                    self.robot.vitesse_droite = self.default_vd
                    self.square_state = 'move'
                    self.current_segment += 1
                    self.segment_start_x = self.robot.x
                    self.segment_start_y = self.robot.y
                    self.segment_travelled = 0
                    if self.current_segment >= 4:
                        print("Carré terminé")
                        running = False

            if self.detecter_collision(self.robot.x, self.robot.y):
                print("Obstacle détecté, arrêt du carré")
                running = False

            ir_point = self.robot.scan_infrarouge(self.obstacles, IR_MAX_DISTANCE)
            distance_ir = math.hypot(ir_point[0] - self.robot.x, ir_point[1] - self.robot.y)
            self.affichage.mettre_a_jour(self.robot, ir_point, distance_ir)
            pygame.display.flip()
            pygame.time.delay(30)
        print("Fin du mode carré")

