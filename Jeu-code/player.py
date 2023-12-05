import pygame







class Player(pygame.sprite.Sprite):
    #cette fonction initialise les attributs qui sont dans la classe Player
    def __init__(self):
        super().__init__()
        self.marioMvmt_img = pygame.image.load("images/mario_mvmt1.png")
        self.marioSaut_img = pygame.image.load("images/mario_saut.png")

        self.mario_run = True
        self.mario_jump = False
        self.cpt = 0
        self.saut_vel = 8
        self.image = self.marioMvmt_img
        self.mario_rect = self.image.get_rect()
        self.mario_rect.x = 0
        self.mario_rect.y = 0

    #fonction de mise a jour qui modifie le jeu par rapport aux actions du joueur
    def update(self):
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
        # Initialise l'image à celle qui correspond au saut de mario
        self.image = self.marioSaut_img
        # Si mario saute
        if self.mario_jump:
            # Initialise le rect pour gérer les collisions
            self.mario_rect = self.image.get_rect()
            # Ajuste les proportions en hauteur du rectangle de mario change
            # La valeur 5 permet d'avoir la hauteur plus ou moins grande du saut
            self.mario_rect.y -= self.saut_vel * 5
            # Créer une sorte de gravité en enlevant -1 à la vélocité
            self.saut_vel -= 1
            # Si la vélocité du saut est inférieure à -8, on a fini le saut et on le réinitialise à 8
            if self.saut_vel < -8:
                self.mario_jump = False
                self.saut_vel = 8

    #cette fonction affiche dans la fenêtre mario à la position indiqué précédemment
    def draw(self, screen):
        screen.blit(self.image, (self.mario_rect.x, self.mario_rect.y))


"""
#Creer une classe qui va etre le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        self.mario_mvmt = [pygame.image.load("images/mario_mvmt1.png"), pygame.image.load("images/mario_mvmt2.png")]
        self.mario_saut = pygame.image.load("images/mario_saut.png")
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.image = self.mario_mvmt[0]
        self.rect = self.image.get_rect()
        self.rect.y = 500

    def sauter(self):
        if not self.game.check_collision(self, self.game.all_obstacles):
            self.rect.y -= self.velocity


    def collision(self):
        if self.game.check_collision(self, self.game.all_obstacles):
            self.game.game_over()
"""