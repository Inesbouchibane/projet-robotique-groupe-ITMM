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