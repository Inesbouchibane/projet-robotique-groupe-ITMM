import unittest
from robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(100, 100, 1, 1)
    
    def test_deplacement(self):
        x_avant, y_avant = self.robot.x, self.robot.y
        self.robot.deplacer()
        self.assertNotEqual((self.robot.x, self.robot.y), (x_avant, y_avant))
    
    def test_scan_infrarouge(self):
        obstacles = [(200, 200, 50, 50)]
        point_detecte = self.robot.scan_infrarouge(obstacles, 100)
        self.assertIsInstance(point_detecte, tuple)
        self.assertEqual(len(point_detecte), 2)

if __name__ == "__main__":
    unittest.main()

