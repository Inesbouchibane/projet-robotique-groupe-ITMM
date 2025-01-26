# Compte rendu  de la première semaine
Durant cette première semaine, et comme début de travail, nous avons suivi un tutoriel Python pour rafraîchir nos connaissances et avons réalisé quelques exercices pour les appliquer. Cette phase a duré environ 6 heures. Nous avons ensuite commencé par écrire une classe Python représentant un robot capable de se déplacer dans un plan 2D.

Ce travail constitue une introduction à la programmation orientée objet, à la gestion des données et à la visualisation graphique avec Python.

Nous avons créé la fonction approcher pour permettre au robot de se déplacer automatiquement vers le mur le plus proche. Pour cela, nous avons d'abord utilisé la fonction mur_le_plus_proche, qui calcule les distances entre le robot et les bords de l'espace (gauche, droite, haut, bas)(x=0, x=20, y=0, y=20). Cette fonction retourne ensuite la direction du mur le plus proche.
À chaque étape, le robot avance d'un pas grace a la fonction deplacement dans la direction du mur le plus proche. Nous avons mis en place une vérification continue pour nous assurer que le robot s'arrête dès qu'il atteint le mur.



<img width="440" alt="Capture d’écran 2025-01-21 à 21 34 39" src="https://github.com/user-attachments/assets/3abec95b-8505-4bfe-8db1-cfd978cca532" />

![GRAPH](https://github.com/user-attachments/assets/93f97d73-6dfb-42a5-8a2c-6ec2c6e990ee)


