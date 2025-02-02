import unittest
from controleur import Controleur

class TestControleur(unittest.TestCase):
    def setUp(self):
        self.controleur = Controleur(4, 5)

    def test_initialisation(self):
        self.assertEqual(self.controleur.vitesse_gauche, 4)
        self.assertEqual(self.controleur.vitesse_droite, 5)

    def test_ajuster_vitesse(self):
        self.controleur.ajuster_vitesse(2, 3)
        self.assertEqual(self.controleur.vitesse_gauche, 2)
        self.assertEqual(self.controleur.vitesse_droite, 3)

if __name__ == '__main__':
    unittest.main()