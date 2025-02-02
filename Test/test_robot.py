import unittest
from graphisme import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(100, 100, 5, 5)  # Position initiale (100,100) avec vitesses = 5

    def test_initialisation(self):
        self.assertEqual(self.robot.x, 100)
        self.assertEqual(self.robot.y, 100)
        self.assertEqual(self.robot.vitesse_gauche, 5)
        self.assertEqual(self.robot.vitesse_droite, 5)

    def test_deplacement(self):
        self.robot.deplacer()
        self.assertNotEqual(self.robot.x, 100)  # Le robot doit se déplacer
        self.assertNotEqual(self.robot.y, 100)

    def test_changement_vitesse(self):
        self.robot.vitesse_gauche = 2
        self.robot.vitesse_droite = 3
        self.assertEqual(self.robot.vitesse_gauche, 2)
        self.assertEqual(self.robot.vitesse_droite, 3)

if __name__ == '__main__':
    unittest.main()
