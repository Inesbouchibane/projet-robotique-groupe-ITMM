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
        self.obstacles = [(200, 200, 100, 100), (400, 100, 50,50)]
        self.affichage = Affichage(LARGEUR, HAUTEUR, self.obstacles)
        self.avoidance_counter = 0
        # Stocker les vitesses par défaut pour l'évitement et le mode carré
        self.default_vg = vitesse_gauche
        self.default_vd = vitesse_droite

    def detecter_collision(self, x, y):
        for ox, oy, ow, oh in self.obstacles:
            if ox < x < ox + ow and oy < y < oy + oh:
                return True
        return False

    def boucle_principale(self):
        if self.mode == "carré":
            self.dessiner_carre()
            return

        # Modes manuel et automatique
        running = True
        while running:
            # Gestion des événements
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
                            # Demande les nouvelles vitesses sans réinitialiser la position ni la trajectoire
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
                        self.avoidance_counter = 30  # nombre de cycles pour tourner
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
        # Constants for square drawing mode
        SEGMENT_LENGTH = 200   # longueur de chaque segment
        TURN_CYCLES = 30       # nombre de cycles pour tourner 90
        
        # Initialisation des variables de l'état
        if not hasattr(self, 'square_initialized'):
            self.square_state = 'move'      # état : 'move' ou 'turn'
            self.segment_travelled = 0
            self.current_segment = 0
            self.turn_cycles = 0
            self.square_initialized = True
            # On s'assure que les vitesses sont identiques pour aller tout droit
            self.robot.vitesse_gauche = self.default_vg
            self.robot.vitesse_droite = self.default_vd
            # Position de départ du segment
            self.segment_start_x = self.robot.x
            self.segment_start_y = self.robot.y

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            old_x, old_y = self.robot.x, self.robot.y

