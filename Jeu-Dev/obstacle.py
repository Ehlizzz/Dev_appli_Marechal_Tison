import random
import pygame
class Obstacle():
    # Initialisation de l'objet Obstacle
    def __init__(self):
        # Liste des images d'obstacles
        self.imagestock = [pygame.image.load("images/Obstacle-tortue.png"), pygame.image.load("images/Obstacle-tortue1.png"), pygame.image.load("images/Obstacle-tortue2.png"), pygame.image.load("images/Obstacle-tortue3.png"), pygame.image.load("images/Obstacle-tortue4.png")]

        # Choix aléatoire d'une image d'obstacle
        self.image = self.imagestock[random.randint(0, 4)]

        # Redimensionnement de l'image d'obstacle
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Récupération des dimensions de l'image comme une idbox
        self.rect = self.image.get_rect()

        # Position initiale de l'obstacle au spawn
        self.rect.x = 2000 + random.randint(0, 1000)
        self.rect.y = 525

        # Définition de la vitesse des obstacles
        self.velocity = 10 + random.randint(1, 10)

    # Fonction de déplacement qui fait glisser l'obstacle de gauche à droite
    def deplacer(self):
        self.rect.x -= self.velocity

    # Vérification si l'obstacle est hors de l'écran
    def check(self):
        if self.rect.x <= -100:
            return 1

    # Fonction de dessin qui affiche l'obstacle à l'écran
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Fonction de réinitialisation de la position de l'obstacle
    def reset(self):
        self.rect.x = 2000 + random.randint(100, 1000)
