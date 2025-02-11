import pygame
import math
import random

# Dimensions de la fenêtre
LARGEUR = 800
HAUTEUR = 600

# Couleurs
BLANC    = (255, 255, 255)
NOIR     = (0, 0, 0)
BLEU     = (0, 0, 255)
ROUGE    = (255, 0, 0)
VERT     = (0, 255, 0)
CYAN     = (0, 255, 255)
MAGENTA  = (255, 0, 255)

# Paramètres du capteur infrarouge
IR_MAX_DISTANCE = 100  # Portée maximale du capteur en pixels
IR_SEUIL_ARRET  = 50   # Seuil d'arrêt (ou de déclenchement de l'évitement) en pixels

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
        
        # Limiter la position aux bords de la fenêtre
        self.x = max(self.largeur, min(LARGEUR - self.largeur, self.x + dx))
        self.y = max(self.longueur, min(HAUTEUR - self.longueur, self.y + dy))

    def dessiner(self, ecran):
        angle_rad = math.radians(self.angle)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)

        # Calcul des coins du robot pour dessiner un polygone
        points = [
            (self.x + cos_a * self.longueur / 2 - sin_a * self.largeur / 2,
             self.y - sin_a * self.longueur / 2 - cos_a * self.largeur / 2),
            (self.x - cos_a * self.longueur / 2 - sin_a * self.largeur / 2,
             self.y + sin_a * self.longueur / 2 - cos_a * self.largeur / 2),
            (self.x - cos_a * self.longueur / 2 + sin_a * self.largeur / 2,
             self.y + sin_a * self.longueur / 2 + cos_a * self.largeur / 2),
            (self.x + cos_a * self.longueur / 2 + sin_a * self.largeur / 2,
             self.y - sin_a * self.longueur / 2 + cos_a * self.largeur / 2),
        ]

        pygame.draw.polygon(ecran, BLEU, points)
        # Tracer le "nez" du robot
        pointe_x = self.x + cos_a * self.longueur / 2
        pointe_y = self.y - sin_a * self.longueur / 2
        pygame.draw.line(ecran, VERT, (self.x, self.y), (pointe_x, pointe_y), 3)

<<<<<<< HEAD
  def reinitialiser(self):
        """Remet le robot à son état initial. Cette fonction place le robot au centre de la zone de simulation avec un angle nul 
        et remet sa vitesse à zéro."""
        self.x = 400  # Position initiale X
        self.y = 300  # Position initiale Y
        self.vitesse_gauche = 0 
        self.vitesse_droite = 0  
        self.angle = 0 
        self.en_mouvement = True 
=======
    def scan_infrarouge(self, obstacles, max_distance=IR_MAX_DISTANCE, step=5):
        """
        Simule un capteur infrarouge partant du centre du robot dans la direction de son angle.
        On avance par incréments (step) jusqu'à max_distance et on vérifie la collision avec les obstacles.
        Renvoie le point de détection.
        """
        angle_rad = math.radians(self.angle)
        cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
        for d in range(0, int(max_distance), step):
            x_point = self.x + cos_a * d
            y_point = self.y - sin_a * d
            point_rect = pygame.Rect(x_point, y_point, 2, 2)
            for obstacle in obstacles:
                if obstacle.colliderect(point_rect):
                    return (x_point, y_point)
        return (self.x + cos_a * max_distance, self.y - sin_a * max_distance)
>>>>>>> a86882bdcc165be22372201809f8db5f5155064f

class Environnement:
    def __init__(self, vitesse_gauche, vitesse_droite, mode):
        pygame.init()
        self.ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
        pygame.display.set_caption("Simulation de Robot")
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 30)
        self.robot = Robot(LARGEUR / 2, HAUTEUR / 2, vitesse_gauche, vitesse_droite)
        # Stockage des vitesses par défaut pour le mode automatique
        self.default_vg = vitesse_gauche
        self.default_vd = vitesse_droite
        # Mode de fonctionnement : "manuel" ou "automatique"
        self.mode = mode
        # Variables pour le mode automatique
        self.avoidance_mode = False
        self.avoidance_direction = None  # "left" ou "right"
        
        # Obstacles définis par des rectangles
        self.obstacles = [pygame.Rect(200, 200, 100, 100),
                          pygame.Rect(400, 100, 50, 50)]
        self.trajectoire = []

    
    def reinitialiser(self):
        """ Réinitialise l'environnement et le robot """
        self.robot.x = LARGEUR / 2
        self.robot.y = HAUTEUR / 2
        self.robot.angle = 0
        self.robot.vitesse_gauche = self.default_vg
        self.robot.vitesse_droite = self.default_vd
        self.trajectoire = []
        self.avoidance_mode = False
        self.avoidance_direction = None


    def dessiner_obstacles(self):
        for obstacle in self.obstacles:
            pygame.draw.rect(self.ecran, ROUGE, obstacle)

    def detecter_collision(self, x, y):
<<<<<<< HEAD
        """ Vérifie si le robot entre en collision avec un obstacle.La fonction crée un rectangle autour du robot à la position 
donnée et teste s'il intersecte un obstacle."""

      robot_rect = pygame.Rect(x - self.robot.largeur, y - self.robot.longueur, self.robot.largeur * 2, self.robot.longueur * 2)
=======
        """
        Vérifie si le rectangle englobant le robot en position (x, y)
        entre en collision avec un obstacle.
        """
        robot_rect = pygame.Rect(x - self.robot.largeur,
                                 y - self.robot.longueur,
                                 self.robot.largeur * 2,
                                 self.robot.longueur * 2)
>>>>>>> a86882bdcc165be22372201809f8db5f5155064f
        for obstacle in self.obstacles:
            if robot_rect.colliderect(obstacle):
                return True
        return False

    def boucle_principale(self):
        running = True
        while running:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # En mode manuel, l'utilisateur peut ajuster ou arrêter
                    if self.mode == "manuel":
                        if event.key == pygame.K_s:
                            self.robot.en_mouvement = False
                        elif event.key == pygame.K_d:
                            try:
                                self.robot.vitesse_gauche = float(input("Entrez la vitesse de la roue gauche : "))
                                self.robot.vitesse_droite = float(input("Entrez la vitesse de la roue droite : "))
                            except ValueError:
                                print("Veuillez entrer des valeurs numériques valides.")
                            self.robot.en_mouvement = True
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.reinitialiser()


            if self.robot.en_mouvement:
                # Calcul de la distance détectée par le capteur infrarouge
                ir_point = self.robot.scan_infrarouge(self.obstacles)
                distance_ir = math.hypot(ir_point[0] - self.robot.x, ir_point[1] - self.robot.y)

                # Préparation de l'affichage de la distance
                distance_text = self.font.render(f"Distance: {round(distance_ir,2)} px", True, NOIR)
                
                # Selon le mode choisi, le comportement diffère
                if self.mode == "automatique":
                    # En mode automatique, si le capteur détecte un obstacle trop proche
                    # ou si une collision imminente est détectée, on active l'évitement
                    vitesse_moyenne = (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2
                    delta_angle = (self.robot.vitesse_droite - self.robot.vitesse_gauche) / self.robot.largeur * 10

                    # Calcul de la position future (si on ne modifiait pas la trajectoire)
                    dx = vitesse_moyenne * math.cos(math.radians(self.robot.angle))
                    dy = -vitesse_moyenne * math.sin(math.radians(self.robot.angle))
                    new_robot_x = self.robot.x + dx
                    new_robot_y = self.robot.y + dy
                    collision_obstacle = self.detecter_collision(new_robot_x, new_robot_y)
                    collision_mur = (new_robot_x <= self.robot.largeur or 
                                     new_robot_x >= LARGEUR - self.robot.largeur or 
                                     new_robot_y <= self.robot.longueur or 
                                     new_robot_y >= HAUTEUR - self.robot.longueur)

                    if distance_ir < IR_SEUIL_ARRET or collision_obstacle or collision_mur:
                        if not self.avoidance_mode:
                            # Choix aléatoire de tourner à gauche ou à droite
                            self.avoidance_direction = random.choice(["left", "right"])
                            self.avoidance_mode = True
                        # Appliquer la manœuvre d'évitement : rotation sur place
                        if self.avoidance_direction == "left":
                            self.robot.vitesse_gauche = -abs(self.default_vg)
                            self.robot.vitesse_droite = abs(self.default_vd)
                        else:
                            self.robot.vitesse_gauche = abs(self.default_vg)
                            self.robot.vitesse_droite = -abs(self.default_vd)
                    else:
                        # Si aucun obstacle n'est détecté et si l'on était en mode évitement,
                        # revenir aux vitesses par défaut
                        if self.avoidance_mode:
                            self.robot.vitesse_gauche = self.default_vg
                            self.robot.vitesse_droite = self.default_vd
                            self.avoidance_mode = False
                    # Dans tous les cas, calculer la nouvelle position à partir des vitesses actuelles
                    vitesse_moyenne = (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2
                    delta_angle = (self.robot.vitesse_droite - self.robot.vitesse_gauche) / self.robot.largeur * 10
                    self.robot.angle += delta_angle
                    self.robot.angle %= 360
                    dx = vitesse_moyenne * math.cos(math.radians(self.robot.angle))
                    dy = -vitesse_moyenne * math.sin(math.radians(self.robot.angle))
                    new_robot_x = self.robot.x + dx
                    new_robot_y = self.robot.y + dy
                    # Mise à jour de la position
                    self.robot.x = max(self.robot.largeur, min(LARGEUR - self.robot.largeur, new_robot_x))
                    self.robot.y = max(self.robot.longueur, min(HAUTEUR - self.robot.longueur, new_robot_y))
                    self.trajectoire.append((self.robot.x, self.robot.y))
                else:
                    # Mode manuel (version actuelle) : si un obstacle est détecté,
                    # le robot s'arrête et affiche la distance dans la console
                    vitesse_moyenne = (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2
                    delta_angle = (self.robot.vitesse_droite - self.robot.vitesse_gauche) / self.robot.largeur * 10
                    self.robot.angle += delta_angle
                    self.robot.angle %= 360
                    dx = vitesse_moyenne * math.cos(math.radians(self.robot.angle))
                    dy = -vitesse_moyenne * math.sin(math.radians(self.robot.angle))
                    new_robot_x = self.robot.x + dx
                    new_robot_y = self.robot.y + dy

                    collision_obstacle = self.detecter_collision(new_robot_x, new_robot_y)
                    collision_mur = (new_robot_x <= self.robot.largeur or 
                                     new_robot_x >= LARGEUR - self.robot.largeur or 
                                     new_robot_y <= self.robot.longueur or 
                                     new_robot_y >= HAUTEUR - self.robot.longueur)
                    if distance_ir < IR_SEUIL_ARRET or collision_obstacle or collision_mur:
                        print(f"Obstacle détecté! Distance = {round(distance_ir,2)} pixels")
                        self.robot.en_mouvement = False
                    else:
                        self.robot.x = new_robot_x
                        self.robot.y = new_robot_y
                        self.trajectoire.append((self.robot.x, self.robot.y))
                
                # Mise à jour de l'affichage
                self.ecran.fill(BLANC)
                self.dessiner_obstacles()
                self.robot.dessiner(self.ecran)
                self.dessiner_trajectoire()
                pygame.draw.line(self.ecran, CYAN, (self.robot.x, self.robot.y), ir_point, 2)
                pygame.draw.circle(self.ecran, MAGENTA, (int(ir_point[0]), int(ir_point[1])), 5)
                self.ecran.blit(distance_text, (10, 10))
            
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

<<<<<<< HEAD
#--------------------------------------------------Takoua--------------------------------------------------------------------------
    def mettre_a_jour_position(self):
        """Met à jour la position du robot en fonction de ses vitesses et détecte les collisions."""
        if self.robot.en_mouvement:
            new_x = self.robot.x
            new_y = self.robot.y
            vitesse_moyenne = (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2
            delta_angle = (self.robot.vitesse_droite - self.robot.vitesse_gauche) / self.robot.largeur * 10

            self.robot.angle += delta_angle
            self.robot.angle %= 360

            dx = vitesse_moyenne * math.cos(math.radians(self.robot.angle))
            dy = -vitesse_moyenne * math.sin(math.radians(self.robot.angle))

            if not self.detecter_collision(new_x + dx, new_y + dy):
                self.robot.x = max(self.robot.largeur, min(LARGEUR - self.robot.largeur, new_x + dx))
                self.robot.y = max(self.robot.longueur, min(HAUTEUR - self.robot.longueur, new_y + dy))


    def mettre_a_jour_affichage(self):
        """Met à jour l'affichage en redessinant les éléments."""
        self.ecran.fill(BLANC)
        self.dessiner_obstacles()
        self.robot.dessiner(self.ecran)
        pygame.display.flip()


    def dessiner_trajectoire(self):   
        """ Cette fonction dessine la trah=jecetoire du robot en temps réel"""
=======
    def dessiner_trajectoire(self):
>>>>>>> a86882bdcc165be22372201809f8db5f5155064f
        if len(self.trajectoire) > 1:
            pygame.draw.lines(self.ecran, NOIR, False, self.trajectoire, 2)
