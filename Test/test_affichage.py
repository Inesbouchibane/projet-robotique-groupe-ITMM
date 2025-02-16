import unittest
from unittest.mock import MagicMock, patch
import pygame
from affichage import Affichage
from robot import Robot
import math

# Constantes pour simuler l'environnement
LARGEUR = 800
HAUTEUR = 600
OBSTACLES = [(200, 200, 100, 100), (400, 300, 50, 50)]  # Liste d'obstacles
