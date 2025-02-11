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
        for ox, oy, ow, oh in self.obstacles:
            pygame.draw.rect(self.ecran, ROUGE, (ox, oy, ow, oh))
        pygame.draw.polygon(self.ecran, BLEU, self.calculer_points_robot(robot))
        pygame.draw.line(self.ecran, VERT, (robot.x, robot.y), ir_point, 2)
        pygame.draw.circle(self.ecran, MAGENTA, (int(ir_point[0]), int(ir_point[1])), 5)
        text = self.font.render(f"Distance: {round(distance_ir,2)} px", True, NOIR)
        self.ecran.blit(text, (10, 10))
        
        pygame.display.flip()
        self.clock.tick(30)

