# Compte rendu de la semaine 2

**Objectif de la Semaine :**  
Cette semaine, l’objectif principal était de rattraper notre retard sur la compréhension et l’utilisation de GitHub, ainsi que de poursuivre le développement du robot en 2D. Cela impliquait de comprendre les concepts liés à la gestion de version et de finaliser les fonctionnalités principales permettant au robot de se déplacer et d’interagir avec son environnement.

**Travail Réalisé :**   

Durant cette deuxième semaine, nous avons tout d'abord suivi un tutorial expliquant le bon fonctionnement de github et cela en visionnant ces deux videos :  
https://youtu.be/X3KCX99I2pQ?si=ylpYr9W0juybpYoQ  
https://youtu.be/X3KCX99I2pQ?si=ylpYr9W0juybpYoQ

Nous avons structuré notre  projet en deux classes principales : Robot et Environnement.
La classe Robot: représente un robot autonome sur un canvas graphique , elle est le cœur de notre projet. Elle définit les propriétés et les actions du robot, comme expliqué ci-dessous :
    Initialisation (__init__) : Le robot est placé sur un canvas à une position initiale (x, y), avec une vitesse définie. Un cercle bleu représente le robot, accompagné d'une ligne qui indique sa direction.
    Déplacement (deplacer) : Cette méthode déplace le robot en fonction de coordonnées (dx, dy), tout en vérifiant qu’il reste à l’intérieur des limites de l’espace défini.
    Avancer vers un mur (avancer_vers_mur) : Une fonctionnalité permettant au robot de calculer et d’avancer automatiquement vers le mur le plus proche à une vitesse donnée.
    Rotation (tourner) : Le robot peut tourner à gauche ou à droite d’un angle défini (par défaut 10°). La ligne de direction est mise à jour pour refléter la nouvelle orientation  

La classe Environnement: Cette classe gère l’espace dans lequel le robot évolue :
    Obstacles : Nous avons ajouté des obstacles fixes sous forme de rectangles rouges sur le canvas. Le robot vérifie les collisions avant chaque mouvement pour éviter de traverser ces obstacles.
    Interaction utilisateur : Grâce aux événements clavier, l’utilisateur peut :
        Déplacer le robot avec les flèches (Haut, Bas, Gauche, Droite).
        Changer la vitesse du robot en appuyant sur la touche v.
        Calculer et avancer vers le mur le plus proche avec la touche m.
        Collision avec les obstacles : La méthode presence_collision détecte si le robot touche un obstacle. Si une collision est détectée, le robot s’arrête.

Nous avons utilisé la bibliothèque Tkinter pour afficher graphiquement :

    Le robot, représenté par un cercle bleu avec une ligne indiquant sa direction.
    Les obstacles, représentés par des rectangles rouges.
    Les limites de l’espace, définies par un canvas de 800x600 pixels.    

**Exemple de Scénario d'Utilisation:**
    L'utilisateur peut initialiser le robot à une position de départ centrale.
    En appuyant sur les touches fléchées, il peut déplacer le robot dans différentes directions.
    En appuyant sur m, il peut demander au robot de calculer et de se diriger automatiquement vers le mur le plus proche.
    En appuyant sur v, il peut ajuster la vitesse du robot à tout moment.
   
 
