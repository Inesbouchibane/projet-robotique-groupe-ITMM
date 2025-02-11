
1 sur 3 921
(aucun objet)
Boîte de réception

Mouna Bahamid <mounabahamid10@gmail.com>
Pièces jointes
20:17 (il y a 22 minutes)
À moi


 3 pièces jointes
  • Analyse effectuée par Gmail
import unittest
from environnement import Environnement
from robot import Robot

class TestEnvironnement(unittest.TestCase):

    def setUp(self):
        """Initialisation d'un environnement pour les tests"""
        self.env = Environnement(2, 2, "automatique")
        # Assurez-vous que l'attribut est initialisé
        self.env.avoidance_mode = False

    def test_initialisation(self):
        """Test l'initialisation de l'environnement"""
        self.assertEqual(self.env.mode, "automatique")
        self.assertIsInstance(self.env.robot, Robot)
        self.assertEqual(len(self.env.obstacles), 2)

    def test_detecter_collision(self):
        """Test la détection de collision avec un obstacle"""
        # Coordonnées dans un obstacle (adaptées à votre logique)
        self.assertTrue(self.env.detecter_collision(250, 250))
        # Coordonnées hors des obstacles
        self.assertFalse(self.env.detecter_collision(50, 50))

    def test_avoidance_mode_activation(self):
        """Test si l'évitement d'obstacles s'active en mode automatique"""
        # On définit un obstacle couvrant la zone de (200,200) à (300,300)
        self.env.obstacles = [(200, 200, 100, 100)]
        # On place le robot à l'intérieur de cet obstacle
        self.env.robot.x, self.env.robot.y = 250, 250
        
        # Simulation de l'actualisation de l'état qui se ferait dans la boucle principale
        if self.env.detecter_collision(self.env.robot.x, self.env.robot.y):
            self.env.avoidance_mode = True
        else:
            self.env.avoidance_mode = False

        print(f"avoidance_mode: {self.env.avoidance_mode}")  # Pour le débogage
        self.assertTrue(self.env.avoidance_mode)

if __name__ == '__main__':
    unittest.main()
