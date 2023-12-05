#importation de pygame
import pygame
pygame.init()
from obstacle import Obstacle
obstacle = Obstacle()
#constante (importation des images)

#creer la taille de la fenêtre du jeu

pygame.mixer.init()

#creer une classe Player où on ajoute les fonctions du joueur
class Player:
    #initialise les variable pour la position de mario
    pos_x = 150
    pos_y = 480
    #cette fonction initialise les attributs qui sont dans la classe Player
    def __init__(self):
        # initialise les 2 images de mario quand il est en mouvement (on cherche l'image dans nos fichiers
        self.mario_mvmt = [pygame.image.load("images/mario_mvmt1.1.png"), pygame.image.load("images/mario_mvmt2.2.png")]
        # initialise l'image de mario quand il saute
        self.mario_saut = pygame.image.load("images/mario_saut.2.png")

        # initialise l'image de fond du jeu
        self.background = [pygame.image.load('images/paysage_mario.png'), pygame.image.load('images/paysage_mariov2.png'), pygame.image.load('images/paysage_mario.png')]
        self.background_rect = self.background[0].get_rect()
        self.background_rect2 = self.background[1].get_rect()
        self.background_rect3 = self.background[2].get_rect()
        self.velocity = 3
        self.marioMvmt_img = self.mario_mvmt
        self.marioSaut_img = self.mario_saut
        self.mario_run = True
        self.mario_jump = False
        self.cpt = 0
        self.saut_vel = 11
        self.image = self.marioMvmt_img[0]
        self.mario_rect = self.image.get_rect()
        self.mario_rect.width -= 1000
        self.mario_rect.x = self.pos_x
        self.mario_rect.y = self.pos_y

    #fonction de mise a jour qui modifie le jeu par rapport aux actions du joueur
    def update(self,input):
        #si mario est en train de courir faire la fonction run
        if self.mario_run:
            self.run()
        # si mario saute faire la fonction saut
        if self.mario_jump:
            self.saut()
        # sert a réinitialisé le pas à 0 quand le pas vaut 8 (permet de créer une sorte de boucle)
        if self.cpt >= 8:
            self.cpt = 0
        #empêche mario de courir quand il saute
        if input[pygame.K_SPACE] and not self.mario_jump:
            self.mario_run = False
            self.mario_jump = True
        #fait courir mario quand il ne saute pas
        elif not(self.mario_jump):
            self.mario_run = True
            self.mario_jump = False
        if self.mario_rect.colliderect(obstacle.rect):
            self.mario_run = False
            self.mario_jump = False


    #gère la course de mario
    def run(self):
        #permet de changer l'image de manière fluide afin que le changement ne soit pas trop rapide
        self.image = self.marioMvmt_img[self.cpt//4]
        #créer un rectangle autour du perso permettant de gérer une rectangle pour les collisions
        self.mario_rect = self.image.get_rect()
        #précise la position x et y du perso
        self.mario_rect.x = self.pos_x
        self.mario_rect.y = self.pos_y
        #ajoute 1 au compteur
        self.cpt += 1

    #gère les saut de mario
    def saut(self):
        #initialise l'image à celle qui correspond au saut de mario
        self.image = self.marioSaut_img
        #si mario saute
        if self.mario_jump:
            #ajuste les proportions en hauteur du rectangle de mario change
            #la valeur 5 permet d'avoir la hauteur plus ou moins grande du saut
            self.mario_rect.y -= self.saut_vel * 5
            #créer une sorte de gravité en enlevant -1 à la vélocité
            self.saut_vel -= 1
            #si la vélocité du saut est inférieur à -8, on a fini le saut et on le réinitialise à 8
            if self.saut_vel < -11:
                self.mario_jump = False
                self.saut_vel = 11

    def draw(self, screen):
        # Affichage des différentes parties du fond et de l'image de Mario
        screen.blit(self.background[0], self.background_rect)
        screen.blit(self.background[1], self.background_rect2)
        screen.blit(self.background[2], self.background_rect3)
        screen.blit(self.image, (self.mario_rect.x, self.mario_rect.y))

    # Fonction pour ajuster la position du fond (défilement)
    def decor(self):
        # Réinitialisation de la position du fond après un certain déplacement
        self.background_rect.y = -80
        self.background_rect2.y = -80
        self.background_rect3.y = -80

        # Ajustement de la position des différents éléments du fond pour créer un effet de défilement
        self.background_rect3.x = self.background_rect2.x + self.background_rect2.width - 5
        self.background_rect2.x = self.background_rect.x + self.background_rect.width - 5
        self.background_rect.x -= self.velocity

        # Réinitialisation de la position du premier fond si le deuxième est hors de l'écran
        if self.background_rect2.x <= -self.background_rect.width:
            self.background_rect.x = 0

    # Fonction pour définir les images et animations de Mario
    def mario(self):
        # Chargement des images de l'animation de déplacement de Mario
        self.mario_mvmt = [pygame.image.load("images/mario_mvmt1.1.png"), pygame.image.load("images/mario_mvmt2.2.png")]

        # Initialisation de l'image de Mario quand il saute
        self.mario_saut = pygame.image.load("images/mario_saut.2.png")

        # Attribution des images à leurs variables correspondantes
        self.marioMvmt_img = self.mario_mvmt
        self.marioSaut_img = self.mario_saut

    # Fonction pour définir les images et animations de Luigi
    def luigi(self):
        # Chargement des images de l'animation de déplacement de Luigi
        self.mario_mvmt = [pygame.image.load("images/luigi_mvt.png"), pygame.image.load("images/luigi_mvt1.png")]

        # Initialisation de l'image de Luigi quand il saute
        self.mario_saut = pygame.image.load("images/luigi_saut.png")

        # Attribution des images à leurs variables correspondantes
        self.marioMvmt_img = self.mario_mvmt
        self.marioSaut_img = self.mario_saut

