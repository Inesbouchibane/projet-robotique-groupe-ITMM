import unittest
from unittest.mock import MagicMock
from controleur import Controleur
from environnement import Environnement

class TestControleur(unittest.TestCase):
    
    def setUp(self):
        self.env_mock = MagicMock(spec=Environnement)  # Mock de l'environnement
        self.env_mock.robot = MagicMock()  # Mock du robot
        self.controleur = Controleur(5, 5, "automatique")
        self.controleur.env = self.env_mock  # Remplace l'environnement réel par un mock
    
    def test_demarrer_simulation(self):
        self.controleur.demarrer_simulation()
        self.env_mock.boucle_principale.assert_called_once()
    
    def test_ajuster_vitesse(self):
        self.controleur.ajuster_vitesse(3, 4)
        self.assertEqual(self.controleur.vitesse_gauche, 3)
        self.assertEqual(self.controleur.vitesse_droite, 4)
        self.assertEqual(self.env_mock.robot.vitesse_gauche, 3)
        self.assertEqual(self.env_mock.robot.vitesse_droite, 4)
    
    def test_verifier_limite_carre(self):
        self.controleur.distance_parcourue = 10
        self.controleur.longueur_cote = 10
        self.controleur.etape_carre = 0
        self.controleur.robot = MagicMock()  # Mock du robot
        self.controleur.verifier_limite_carre()
        self.assertEqual(self.controleur.etape_carre, 1)
        self.controleur.robot.vitesse_gauche = -2
        self.controleur.robot.vitesse_droite = 2

if __name__ == "__main__":
    unittest.main()