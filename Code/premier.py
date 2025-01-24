import matplotlib.pyplot as plt

class Robot:
    def __init__(self, x=5, y=5, espace=(20, 20)):
        """
        Initialise un robot avec une position initiale (x, y) dans un espace défini.
       
        :param x: Position initiale en x.
        :param y: Position initiale en y.
        :param espace: Dimensions de l'espace (largeur, hauteur).
        """
        self.x = x
        self.y = y
        self.espace = espace  # Dimensions de l'espace (largeur, hauteur)
        self.history = [(x, y)]  # Historique des positions

    def mur_le_plus_proche(self):
        """
        Détermine la direction vers le mur le plus proche.
       
        :return: Direction vers le mur sous forme d'une chaîne ("haut", "bas", "gauche", "droite").
        """
        distances = {
            "gauche": self.x,
            "droite": self.espace[0] - self.x,
            "bas": self.y,
            "haut": self.espace[1] - self.y
        }
        # Trouve la direction avec la distance minimale
        return min(distances, key=distances.get)

    def deplacement(self, direction, step=1):
        """
        Déplace le robot dans une direction spécifique d'un pas.
       
        :param direction: La direction du déplacement ("haut", "bas", "gauche", "droite").
        :param step: Distance à parcourir (par défaut 1).
        """
        if direction == "gauche":
            self.x = max(0, self.x - step)
        elif direction == "droite":
            self.x = min(self.espace[0], self.x + step)
        elif direction == "haut":
            self.y = min(self.espace[1], self.y + step)
        elif direction == "bas":
            self.y = max(0, self.y - step)
        self.history.append((self.x, self.y))

    def approcher(self, step=1):
        """
        Approche progressivement du mur le plus proche.
       
        :param step: Pas de déplacement à chaque itération.
        """
        while True:
            direction = self.mur_le_plus_proche()
            print(f"Position actuelle : ({self.x}, {self.y}) -> Direction : {direction}")
           
            # Vérifie si le robot est arrivé contre un mur
            if (
                (direction == "gauche" and self.x == 0) or
                (direction == "droite" and self.x == self.espace[0]) or
                (direction == "haut" and self.y == self.espace[1]) or
                (direction == "bas" and self.y == 0)
            ):
                print("Le robot a atteint le mur le plus proche.")
                break

            # Déplace le robot dans la direction calculée
            self.deplacement(direction, step)

    def afficher_deplacement(self):
        """
        Affiche le déplacement du robot avec les murs sur un graphe.
        """
        x_vals, y_vals = zip(*self.history)

        plt.figure(figsize=(8, 8))
        # Dessiner les murs (bords de l'espace)
        plt.plot([0, self.espace[0], self.espace[0], 0, 0],
                 [0, 0, self.espace[1], self.espace[1], 0],
                 color='black', linewidth=2, label='Murs')  # Contour des murs
       
        # Trajectoire
        plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='b', label='Trajectoire')
        plt.scatter(x_vals[0], y_vals[0], color='green', label='Départ', s=100)  # Point de départ
        plt.scatter(x_vals[-1], y_vals[-1], color='red', label='Arrivée', s=100)  # Point d'arrivée

        # Titres et configuration du graphique
        plt.title('Déplacement du robot vers le mur le plus proche')
        plt.xlim(0, self.espace[0])
        plt.ylim(0, self.espace[1])
        plt.xlabel('Position X')
        plt.ylabel('Position Y')
        plt.legend()
        plt.grid(True)
        plt.show()


# Exemple d'utilisation
if __name__ == "__main__":
    # Initialiser le robot dans un espace de 20x20 unités
    robot = Robot(x=7, y=12, espace=(20, 20))

    print("Position initiale :", robot.x, robot.y)

    # Approcher le mur le plus proche
    robot.approcher(step=2)

    print("Position finale :", robot.x, robot.y)

    # Afficher le graphe des déplacements
    robot.afficher_deplacement()
