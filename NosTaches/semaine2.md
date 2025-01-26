# Compte rendu de la semaine 2

Classe Robot :
La classe Robot représente un robot autonome sur un canvas graphique.Elle gère ses propriétés principales, comme la position, la vitesse et l'orientation, 
tout en offrant des méthodes pour déplacer, tourner et afficher graphiquement le robot.Cette classe est responsable de toutes les interactions liées au comportement individuel du robot.

Voici les fonctions de notre classe Robot :
   * Initialisation du Robot : Configure les attributs du robot, notamment sa position, sa vitesse, son orientation, et sa représentation visuelle sur le canvas.
   * Déplacement du Robot : Permet au robot de se déplacer (en avant ou en arrière) tout en respectant les limites de l’environnement et les obstacles.
   * Rotation du Robot : Ajuste l’orientation du robot et met à jour visuellement sa direction sur le canvas.
     
Classe Environnement :
La classe Environnement configure le cadre global de la simulation, comprenant le canvas, les obstacles, et les événements clavier pour piloter le robot. 
Elle gère les interactions entre le robot et son environnement, comme la détection de collisions et le calcul des distances vers les murs. 
Cette classe orchestre l'ensemble de la simulation en lançant et maintenant l'interface utilisateur.

Voici les fonctions de notre classe Environnement :
  * Configuration de l’Interface : Met en place le canvas graphique, lie les événements clavier pour le contrôle du robot, et initialise la simulation.
  * Ajout d’Obstacles : Permet de placer des obstacles dans l’environnement et de les enregistrer pour vérifier les interactions.
  * Détection de Collisions : Vérifie si le robot entre en conflit avec un obstacle lors de ses déplacements.
  * Interaction avec les Murs : Calcule les distances aux murs, identifie le mur le plus proche et déplace le robot vers celui-ci sur demande.

