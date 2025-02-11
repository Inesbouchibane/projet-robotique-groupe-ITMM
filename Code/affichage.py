import pygame

class Affichage:
    
        # Affichage des informations (mode et vitesse des roues)
        texte = f"Mode: {mode} | Vitesse Gauche: {robot.vitesse_gauche} | Vitesse Droite: {robot.vitesse_droite}"
        texte_surface = self.font.render(texte, True, (0, 0, 0))
        self.ecran.blit(texte_surface, (10, 10))  # Affichage en haut à gauche

        pygame.display.flip()  # Mettre à jour l'affichage
