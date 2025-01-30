import pygame

def gerer_evenements(robot):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                robot.en_mouvement = False
            elif event.key == pygame.K_d:
                robot.vitesse_gauche = float(input("Entrez la vitesse de la roue gauche : "))
                robot.vitesse_droite = float(input("Entrez la vitesse de la roue droite : "))
                robot.en_mouvement = True
    return True
