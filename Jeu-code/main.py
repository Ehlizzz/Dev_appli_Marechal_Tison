import pygame
pygame.init()
from game import Game
from accueil import Accueil

# Generer la fenetre du jeu
pygame.display.set_caption("Jeu dev appli")
screen = pygame.display.set_mode((1080, 720))

#Importer l'arriere plan
background = pygame.image.load("Assets/bg.jpg")

#Charger le jeu
game = Game()

#charger l'acceuil
accueil = Accueil(game)



running = True
#Boucle run
while running:



    if game.jeustarting == True:
        # appliquer l'arriere plan
        screen.blit(background, (0, -200))
        game.update(screen)

    else:
        accueil.show_accueil()
        accueil.bouton_selection()
        accueil.bouton_start()




    #Mettre a jour l'ecran
    pygame.display.flip()

    #Si la fenetre est ferme
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        #Detecter si la touche a été touché
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False