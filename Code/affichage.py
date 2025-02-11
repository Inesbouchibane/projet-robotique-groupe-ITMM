import pygame

class Affichage:
    def __init__(self, largeur, hauteur, obstacles):
        self.largeur = largeur
        self.hauteur = hauteur
        self.obstacles = obstacles
        pygame.init()
        self.ecran = pygame.display.set_mode((largeur, hauteur))
        self.font = pygame.font.Font(None, 24)  # Police pour afficher le texte

    def mettre_a_jour(self, robot, ir_point, distance_ir, mode):
        self.ecran.fill((255, 255, 255))  # Effacer l'écran
        pygame.draw.circle(self.ecran, (0, 0, 255), (int(robot.x), int(robot.y)), 10)   # Dessiner le robot
       
        # Dessiner les obstacles
        for ox, oy, ow, oh in self.obstacles:
            pygame.draw.rect(self.ecran, (255, 0, 0), (ox, oy, ow, oh))

        # Dessiner le point détecté par le capteur infrarouge
        pygame.draw.circle(self.ecran, (0, 255, 0), (int(ir_point[0]), int(ir_point[1])), 5)

        # Affichage des informations (mode et vitesse des roues)
        texte = f"Mode: {mode} | Vitesse Gauche: {robot.vitesse_gauche} | Vitesse Droite: {robot.vitesse_droite}"
        texte_surface = self.font.render(texte, True, (0, 0, 0))
        self.ecran.blit(texte_surface, (10, 10))  # Affichage en haut à gauche

        pygame.display.flip()  # Mettre à jour l'affichage