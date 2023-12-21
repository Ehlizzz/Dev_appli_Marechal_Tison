#importation de pygame
import pygame
pygame.init()
from obstacle import Obstacle
obstacle = Obstacle()


#creer une classe Player où on ajoute les fonctions du joueur
class Perso:
    #initialise les variable pour la position du perso
    pos_x = 150
    pos_y = 480
    #cette fonction initialise les attributs qui sont dans la classe Player
    def __init__(self):
        # initialise les 2 images du personnage quand il est en mouvement (on cherche l'image dans nos fichiers)
        # les images sont initialisées sur celle de mario
        self.perso_mvmt = [pygame.image.load("images/mario_mvmt1.1.png"), pygame.image.load("images/mario_mvmt2.2.png")]
        # initialise l'image du perso quand il saute
        # l'image est initialisé sur celle de mario
        self.perso_saut = pygame.image.load("images/mario_saut.2.png")

        # on stocke les images de fond dans un tableau
        self.background = [pygame.image.load('images/paysage_mario.png'), pygame.image.load('images/paysage_mariov2.png'), pygame.image.load('images/paysage_mario.png')]
        #création de rectangle qui ont les dimensions des images
        self.background_rect = self.background[0].get_rect()
        self.background_rect2 = self.background[1].get_rect()
        self.background_rect3 = self.background[2].get_rect()
        #vitesse de déplacement du fond
        self.velocity = 3
        #création de variable qui contient les images des mouvements et des saut
        self.persoMvmt_img = self.perso_mvmt
        self.persoSaut_img = self.perso_saut
        #initialisation de l'état du perso
        self.perso_run = True
        self.perso_jump = False
        self.cpt = 0
        #velocité du saut
        self.saut_vel = 11
        #l'image du mouvement est initialisé à la première image du tableau
        self.image = self.persoMvmt_img[0]
        #création du rectangle qui a les dimensions du personnage
        self.perso_rect = self.image.get_rect()
        #initialise la position du perso au position défini plus haut
        self.perso_rect.x = self.pos_x
        self.perso_rect.y = self.pos_y

    # gère la course de mario
    def run(self):
        # diviser par 4 le compteur permet de ralentir le changement d'images toutes les 4 itérations
        # de 0 à 3 c'est l'image à la position 0 et de 4 à 7
        self.image = self.persoMvmt_img[self.cpt // 4]
        # ajoute 1 au compteur
        self.cpt += 1

    # gère les saut de mario
    def saut(self):
        # initialise l'image à celle qui correspond au saut de mario
        self.image = self.persoSaut_img
        # ajuste les proportions en hauteur du rectangle de mario change
        # la multiplication par 5 permet de sauter plus haut et plus rapidement
        self.perso_rect.y -= self.saut_vel * 5
        # créer une sorte de gravité en enlevant -1 à la vélocité
        self.saut_vel -= 1
        # si le perso revient à sa position initiale en y on arrete le saut et on réinitialise la vélocité du saut à 11
        if self.perso_rect.y == self.pos_y:
            self.perso_jump = False
            self.saut_vel = 11

    #fonction de mise a jour qui modifie le jeu par rapport aux actions du joueur
    def update(self,input):
        #si le personage est en train de courir lancer la fonction run
        if self.perso_run:
            self.run()
        # si mario saute lancer la fonction saut
        if self.perso_jump:
            self.saut()
        # sert a réinitialisé le pas à 0 quand le pas vaut 8 (permet de créer une sorte de boucle)
        if self.cpt == 8:
            self.cpt = 0
        #permet de faire sauter le perso avec la touche espace
        if input[pygame.K_SPACE] :
            self.perso_run = False
            self.perso_jump = True
        #fait courir mario quand il ne saute pas
        elif not self.perso_jump:
            self.perso_run = True
            self.perso_jump = False
        #si le personnage est rentré en collision avec un obstacle, l'image ne bouge plus
        if self.perso_rect.colliderect(obstacle.rect):
            self.perso_run = False
            self.perso_jump = False

    def draw(self, screen):
        # Affichage des différentes parties du fond et de l'image du personnage
        screen.blit(self.background[0], self.background_rect)
        screen.blit(self.background[1], self.background_rect2)
        screen.blit(self.background[2], self.background_rect3)
        screen.blit(self.image, (self.perso_rect.x, self.perso_rect.y))


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
        self.persoMvmt_img = self.mario_mvmt
        self.persoSaut_img = self.mario_saut

    # Fonction pour définir les images et animations de Luigi
    def luigi(self):
        # Chargement des images de l'animation de déplacement de Luigi
        self.luigi_mvmt = [pygame.image.load("images/luigi_mvt.png"), pygame.image.load("images/luigi_mvt1.png")]

        # Initialisation de l'image de Luigi quand il saute
        self.luigi_saut = pygame.image.load("images/luigi_saut.png")

        # Attribution des images à leurs variables correspondantes
        self.persoMvmt_img = self.luigi_mvmt
        self.persoSaut_img = self.luigi_saut

