Compte rendu de la semaine 3:

Objectif de la Semaine :
Cette semaine, notre objectif principal était de faire déplacer le robot de manière continue à l'aide de l’horloge. Nous avons également modifié notre approche en commandant directement le robot en ajustant la vitesse des roues gauche et droite.

Travail Réalisé :

1. Réorganisation du Code
Nous avons structuré notre projet en trois modules distincts :
Graphisme : Gestion de l'affichage du robot et des obstacles avec la bibliothèque Pygame.
Contrôleur : Gestion des déplacements et de la logique du robot.
Main : Point d'entrée du programme, permettant d'initialiser et de démarrer la simulation.

2. Passage de Tkinter à Pygame
Nous avons remplacé Tkinter par Pygame afin d’améliorer la gestion des animations et d’obtenir un rendu plus fluide. Cette transition permet :
Une meilleure prise en charge des collisions et des trajectoires.
Une simulation plus dynamique et plus réaliste.

3. Implémentation du Module Graphisme
Nous avons développé une classe Robot qui assure :
L’affichage du robot en fonction de son orientation et de sa direction.
Le traçage de la trajectoire du robot.
La gestion des obstacles présents dans l’environnement de simulation.

4. Implémentation du Module Contrôleur
Le module Controleur gère les interactions avec le robot, notamment :
L’ajustement de la vitesse des roues gauche et droite pour un déplacement plus précis.
La gestion des collisions avec les obstacles.
La réinitialisation de la simulation.

5. Création d'un Dossier de Tests
Nous avons ajouté un dossier Test contenant des tests unitaires pour vérifier le bon fonctionnement des fonctionnalités du projet. Ces tests nous permettent d’assurer la robustesse du code et d’éviter les erreurs lors des futures modifications.

Exemple de Scénario d’Utilisation :

L’utilisateur initialise le robot à une position de départ.
Il peut ajuster la vitesse des roues gauche et droite pour contrôler sa direction.
Le robot se déplace en continu à l’aide de l’horloge de simulation.
Si un obstacle est détecté, une gestion des collisions est effectuée

 