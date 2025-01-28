import tkinter as tk
from tkinter import simpledialog
import math

class Robot:
    def __init__(self, canvas, x, y, vitesse):
        """
        Initialise un robot sur le canvas.
        :param canvas: Instance du canvas Tkinter.
        :param x: Position initiale en x.
        :param y: Position initiale en y.
        :param vitesse: Vitesse initiale du robot.
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.angle = 0  # Orientation par défaut : 0 (droite)
        self.angle_rad = math.radians(self.angle)

        # Création graphique du robot
        self.graphic = self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="blue")
        self.direction_line = self.canvas.create_line(
            self.x, self.y, self.x + 20 * math.cos(self.angle_rad), self.y - 20 * math.sin(self.angle_rad), fill="black"
        )

    def deplacer(self, dx, dy):
        """Déplace le robot de dx et dy en pixels, en s'assurant qu'il reste dans les limites de la fenêtre."""
        new_x = self.x + dx
        new_y = self.y + dy
        if 10 <= new_x <= 790 and 10 <= new_y <= 590:  # Limites de la fenêtre
            self.x += dx
            self.y += dy

            # Mise à jour de la position graphique
            self.canvas.coords(self.graphic, self.x - 10, self.y - 10, self.x + 10, self.y + 10)
            self.canvas.coords(
                self.direction_line,
                self.x, self.y,
                self.x + 20 * math.cos(self.angle_rad), self.y - 20 * math.sin(self.angle_rad)
            )

    def avancer_vers_mur(self, angle_vers_mur):
        """Avance le robot automatiquement vers le mur le plus proche."""
        dx = self.vitesse * math.cos(math.radians(angle_vers_mur))
        dy = -self.vitesse * math.sin(math.radians(angle_vers_mur))
        self.deplacer(dx, dy)

    def tourner(self, delta_angle):
        """Tourne le robot d'un angle delta_angle (en degrés)."""
        self.angle = (self.angle + delta_angle) % 360
        self.angle_rad = math.radians(self.angle)

        # Mise à jour de la ligne de direction
        self.canvas.coords(
            self.direction_line,
            self.x, self.y,
            self.x + 20 * math.cos(self.angle_rad), self.y - 20 * math.sin(self.angle_rad)
        )

class Environnement:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulation de Robot")
        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="white")
        self.canvas.pack()

        # Demande de la vitesse initiale
        self.vitesse = simpledialog.askfloat("Configuration", "Entrez la vitesse initiale du robot (ex : 5) :", minvalue=0.1)

        if self.vitesse is None:
            self.vitesse = 5.0

        # Création du robot
        self.robot = Robot(self.canvas, 400.0, 300.0, self.vitesse)

        # Liste des obstacles
        self.obstacles = []

        # Liaisons clavier
        self.master.bind("<Up>", self.avancer)
        self.master.bind("<Down>", self.reculer)
        self.master.bind("<Left>", self.tourner_gauche)
        self.master.bind("<Right>", self.tourner_droite)
        self.master.bind("m", self.demander_vers_mur)  # Ajouter l'interruption avec la touche 'M'
        self.master.bind("v", self.changer_vitesse)  # Ajouter l'interruption pour changer la vitesse

    def ajouter_obstacle(self, x1, y1, x2, y2):
        """Ajoute un obstacle rectangulaire à l'environnement."""
        obstacle = self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")
        self.obstacles.append((float(x1), float(y1), float(x2), float(y2)))

    def presence_collision(self, new_x, new_y):
        """
        Vérifie si le robot entre en collision avec un obstacle.
        :param new_x: Nouvelle position x du centre du robot.
        :param new_y: Nouvelle position y du centre du robot.
        :return: True si une collision est détectée, False sinon.
        """
        for x1, y1, x2, y2 in self.obstacles:
            # Vérifie si une partie du robot (cercle de rayon 10) entre en collision
            if (x1 - 10) <= new_x <= (x2 + 10) and (y1 - 10) <= new_y <= (y2 + 10):
                return True
        return False

    def avancer(self, event=None):
        """Fait avancer le robot si aucun obstacle n'est détecté."""
        dx = self.robot.vitesse * math.cos(self.robot.angle_rad)
        dy = -self.robot.vitesse * math.sin(self.robot.angle_rad)
        new_x = self.robot.x + dx
        new_y = self.robot.y + dy
        if not self.presence_collision(new_x, new_y):
            self.robot.deplacer(dx, dy)

    def reculer(self, event=None):
        """Fait reculer le robot si aucun obstacle n'est détecté."""
        dx = -self.robot.vitesse * math.cos(self.robot.angle_rad)
        dy = self.robot.vitesse * math.sin(self.robot.angle_rad)
        new_x = self.robot.x + dx
        new_y = self.robot.y + dy
        if not self.presence_collision(new_x, new_y):
            self.robot.deplacer(dx, dy)

    def tourner_gauche(self, event=None):
        """Tourne le robot vers la gauche."""
        self.robot.tourner(-10)  # Tourne de 10 degrés à gauche

    def tourner_droite(self, event=None):
        """Tourne le robot vers la droite."""
        self.robot.tourner(10)  # Tourne de 10 degrés à droite

    def changer_vitesse(self, event=None):
        """Change la vitesse du robot."""
        nouvelle_vitesse = simpledialog.askfloat("Vitesse", "Entrez la nouvelle vitesse du robot :")
        if nouvelle_vitesse is not None:
            self.robot.vitesse = nouvelle_vitesse

    def demander_vers_mur(self, event=None):
        """Demande à l'utilisateur de calculer et déplacer le robot vers le mur le plus proche."""
        # Demander si l'utilisateur veut savoir où est le mur le plus proche
        reponse = simpledialog.askstring("Action", "Voulez-vous savoir quel est le mur le plus proche ? (Oui/Non)")
        
        if reponse and reponse.lower() == "oui":
            # Calculer la distance aux différents murs (gauche, droite, haut, bas)
            distances = {
                "gauche": self.robot.x - 10,
                "droite": 800 - self.robot.x - 10,
                "haut": self.robot.y - 10,
                "bas": 600 - self.robot.y - 10
            }

            # Trouver le mur le plus proche
            mur_avec_distance = min(distances.items(), key=lambda x: x[1])
            mur, distance = mur_avec_distance

            # Afficher le mur le plus proche et sa distance
            simpledialog.messagebox.showinfo("Mur le plus proche", f"Le mur le plus proche est : {mur} à {distance:.2f} pixels.")

            # Demander à l'utilisateur s'il veut avancer vers le mur
            reponse_avancer = simpledialog.askstring("Action", f"Voulez-vous avancer vers le mur {mur} ? (Oui/Non)")
            if reponse_avancer and reponse_avancer.lower() == "oui":
                # Calculer l'angle vers le mur et avancer jusqu'à la bordure
                if mur == "gauche":
                    self.robot.x = 10  # Déplacer le robot jusqu'au bord gauche
                elif mur == "droite":
                    self.robot.x = 790  # Déplacer le robot jusqu'au bord droit
                elif mur == "haut":
                    self.robot.y = 10  # Déplacer le robot jusqu'au bord haut
                elif mur == "bas":
                    self.robot.y = 590  # Déplacer le robot jusqu'au bord bas

                # Mettre à jour la position graphique du robot pour toucher le mur
                self.canvas.coords(self.robot.graphic, self.robot.x - 10, self.robot.y - 10, self.robot.x + 10, self.robot.y + 10)
                self.canvas.coords(
                    self.robot.direction_line,
                    self.robot.x, self.robot.y,
                    self.robot.x + 20 * math.cos(self.robot.angle_rad), self.robot.y - 20 * math.sin(self.robot.angle_rad)
                )

if __name__ == "__main__":
    root = tk.Tk()
    simulation = Environnement(root)

    # Ajout d'obstacles
    simulation.ajouter_obstacle(200.0, 200.0, 300.0, 300.0)
    simulation.ajouter_obstacle(400.0, 100.0, 450.0, 150.0)

    root.mainloop()
