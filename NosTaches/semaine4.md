Cette semaine, nous avons poursuivi l'amélioration de la structure du 
projet en vue de le rendre plus modulaire et facile à maintenir. Nous 
avons commencé par créer une nouvelle branche Git pour sauvegarder l'état 
actuel du code, ce qui nous permet de travailler en toute sécurité sur de 
nouvelles fonctionnalités sans risquer d'endommager la version stable. 

Ensuite, nous avons restructuré la gestion de Pygame en centralisant toute 
la logique d'affichage dans une seule fonction et le fichier graphisme.py 
a été restructuré pour que l'affichage soit indépendant du reste de la 
logique.

Nous avons également adapté le contrôleur pour qu'il puisse fonctionner 
avec ou sans affichage. Une nouvelle fonctionnalité: tracer_carré, a été 
implémentée dans le contrôleur, permettant au robot de dessiner un carré en se déplaçant de manière autonome.

En parallèle, nous avons commencé à modifier les tests unitaires pour 
qu'ils s'adaptent aux nouvelles fonctionnalités et à la structure 
refactorisée.

