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
        self.assertEqual(len(self.env.obstacles), 2


    def test_detecter_collision(self):
        """Test la détection de collision avec un obstacle"""
        # Coordonnées dans un obstacle (adaptées à votre logique)
        self.assertTrue(self.env.detecter_collision(250, 250))
        # Coordonnées hors des obstacles
        self.assertFalse(self.env.detecter_collision(50, 50))