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
    def tracer_carre(self, cote):
        """
        Fait tracer un carré de côté donné par le robot.
        """
        if not self.verifier_limite_carre(cote):
            print("Impossible de tracer le carré : obstacle détecté.")
            return
    
        vitesse = 1.0  # Vitesse constante
        
        for _ in range(4):
            # Avancer d'un côté du carré
            debut_x, debut_y = self.robot.x, self.robot.y
            distance_parcourue = 0
            
            while distance_parcourue < cote:
                # Calculer la distance restante à parcourir
                distance_a_parcourir = min(vitesse, cote - 
distance_parcourue)
                
                # Mettre à jour la position du robot
                dx = distance_a_parcourir * 
math.cos(math.radians(self.robot.angle))
                dy = -distance_a_parcourir * 
math.sin(math.radians(self.robot.angle))
                
                nouvelle_x = self.robot.x + dx
                nouvelle_y = self.robot.y + dy
                
                # Vérifier si la nouvelle position est valide (pas de 
collision)
                if not self.environnement.detecter_collision(nouvelle_x, 
nouvelle_y):
                    self.robot.x = nouvelle_x
                    self.robot.y = nouvelle_y
                    self.environnement.trajectoire.append((self.robot.x, 
self.robot.y))
                    distance_parcourue += distance_a_parcourir
                else:
                    print("Obstacle détecté pendant le tracé du carré. 
Arrêt du tracé.")
                    return
                    
                # Mettre à jour l'affichage
                ir_point = 
self.robot.scan_infrarouge(self.environnement.obstacles, IR_MAX_DISTANCE)
                distance_ir = math.hypot(ir_point[0] - self.robot.x, 
ir_point[1] - self.robot.y)
                self.environnement.affichage.mettre_a_jour(self.robot, 
ir_point, distance_ir, "manuel", self.environnement.trajectoire)
                pygame.time.delay(30)
            
            # Rotation de 90 degrés
            self.robot.angle = (self.robot.angle + 90) % 360


