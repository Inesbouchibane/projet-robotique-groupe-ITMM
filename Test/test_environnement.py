import unittest
from graphisme import Environnement

class TestEnvironnement(unittest.TestCase):
    def setUp(self):
        self.env = Environnement(2, 3)

    def test_initialisation(self):
        self.assertIsNotNone(self.env.robot)  # Vérifier que le robot est bien créé
        self.assertEqual(self.env.robot.vitesse_gauche, 2)
        self.assertEqual(self.env.robot.vitesse_droite, 3)

    def test_detection_collision(self):
        # Vérifier que le robot détecte bien une collision
        self.assertTrue(self.env.detecter_collision(200, 200))  # Il y a un obstacle ici
        self.assertFalse(self.env.detecter_collision(50, 50))   # Aucun obstacle ici

if __name__ == '__main__':
    unittest.main()