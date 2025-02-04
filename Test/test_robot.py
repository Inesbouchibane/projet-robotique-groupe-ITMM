import unittest
from graphisme import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(400, 300, 0, 0)
    
    def test_initialisation(self):
        self.assertEqual(self.robot.x, 400)
        self.assertEqual(self.robot.y, 300)
        self.assertEqual(self.robot.vitesse_gauche, 0)
        self.assertEqual(self.robot.vitesse_droite, 0)
        self.assertEqual(self.robot.angle, 0)
        self.assertTrue(self.robot.en_mouvement)
    
    def test_reinitialiser(self):
        self.robot.x = 100
        self.robot.y = 200
        self.robot.vitesse_gauche = 5
        self.robot.vitesse_droite = 5
        self.robot.angle = 90
        self.robot.en_mouvement = False

        self.robot.reinitialiser()

        self.assertEqual(self.robot.x, 400)
        self.assertEqual(self.robot.y, 300)
        self.assertEqual(self.robot.vitesse_gauche, 0)
        self.assertEqual(self.robot.vitesse_droite, 0)
        self.assertEqual(self.robot.angle, 0)
        self.assertTrue(self.robot.en_mouvement)
    
    def test_deplacement(self):
        self.robot.vitesse_gauche = 2
        self.robot.vitesse_droite = 2
        initial_x = self.robot.x
        initial_y = self.robot.y
        
        self.robot.x += (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2
        self.robot.y += (self.robot.vitesse_gauche + self.robot.vitesse_droite) / 2
        
        self.assertNotEqual(self.robot.x, initial_x)
        self.assertNotEqual(self.robot.y, initial_y)

if __name__ == '__main__':
    unittest.main()
