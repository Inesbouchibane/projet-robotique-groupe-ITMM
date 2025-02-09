import math

class Robot:
    def __init__(self, x, y, vitesse_gauche, vitesse_droite):
        self.x, self.y = x, y
        self.vitesse_gauche = vitesse_gauche
        self.vitesse_droite = vitesse_droite
        self.angle = 0
        self.largeur, self.longueur = 20, 40

    def scan_infrarouge(self, obstacles, max_distance):
        angle_rad = math.radians(self.angle)
        for d in range(0, int(max_distance), 5):
            x_point, y_point = self.x + d * math.cos(angle_rad), self.y - d * math.sin(angle_rad)
            for ox, oy, ow, oh in obstacles:
                if ox < x_point < ox + ow and oy < y_point < oy + oh:
                    return (x_point, y_point)
        return (self.x + max_distance * math.cos(angle_rad), self.y - max_distance * math.sin(angle_rad))
