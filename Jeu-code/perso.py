#importation de pygame
import pygame
pygame.init()

#constante (importation des images)

#creer la taille de la fenêtre du jeu
screen = pygame.display.set_mode((1080, 608))
#initialise les 2 images de mario quand il est en mouvement (on cherche l'image dans nos fichiers
mario_mvmt = [pygame.image.load("../images/mario_mvmt1.png"),
         pygame.image.load("../images/mario_mvmt2.png")]
#initialise l'image de mario quand il saute
mario_saut = pygame.image.load("../images/mario_saut.png")
#initialise l'image de fond du jeu
background = pygame.image.load('../images/paysage_mario.jpg')

#creer une classe Player où on ajoute les fonctions du joueur
class Player:
    #initialise les variable pour la position de mario
    pos_x = 60
    pos_y = 400
    #cette fonction initialise les attributs qui sont dans la classe Player
    def __init__(self):
        self.marioMvmt_img = mario_mvmt
        self.marioSaut_img = mario_saut
        self.mario_run = True
        self.mario_jump = False
        self.cpt = 0
        self.saut_vel = 8
        self.image = self.marioMvmt_img[0]
        self.mario_rect = self.image.get_rect()
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
            if self.saut_vel < -8:
                self.mario_jump = False
                self.saut_vel = 8

    #cette fonction affiche dans la fenêtre mario à la position indiqué précédemment
    def draw(self, screen):
        screen.blit(self.image, (self.mario_rect.x, self.mario_rect.y))

#fonction principale
def main():
    run = True
    temps = pygame.time.Clock()
    player = Player()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((255, 255, 255))
        input = pygame.key.get_pressed()
        screen.blit(background, (0, 0))
        player.draw(screen)
        player.update(input)
        temps.tick(30)
        pygame.display.update()
        #pygame.display.flip()
main()




