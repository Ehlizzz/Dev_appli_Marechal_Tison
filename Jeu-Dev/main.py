
from perso import Player
from obstacle import Obstacle
from accueil import Accueil
from score import Score
import pygame


# Initialisation de la fenêtre de jeu avec une résolution de 1080x720 pixels
if __name__ == '__main__':
    screen = pygame.display.set_mode((1280, 720))
    run = True  # Variable de boucle principale
    temps = pygame.time.Clock()
    pygame.mixer.init()


    player = Player()  # Initialisation du joueur
    accueil = Accueil()  # Initialisation de l'écran d'accueil

    score = Score()  # Initialisation du système de score

    obstacles = []  # Liste pour stocker les obstacles

    # Boucle principale du jeu
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Arrêt du jeu en cas de fermeture de la fenêtre

        screen.fill('black')  # Remplissage de l'écran avec une couleur noire

        input = pygame.key.get_pressed() #Recupere les touches saisies

        screen.blit(player.background[0], (0, -80))  # Affichage du fond

        # Vérification si l'écran d'accueil est en cours
        if not accueil.gamerun:
            if accueil.selection == 0:
                player.mario()  # selectionne Mario sur l'écran d'accueil
            else:
                player.luigi()  # selectionne luigi sur l'écran d'accueil

            accueil.show_accueil(screen)  # Affichage de l'écran d'accueil
            score.draw_score_high(screen)  # Affichage du score le plus élevé
            accueil.bouton_selection()  # Gestion du bouton de selection
            accueil.bouton_start()  # Gestion du bouton de démarrage
            obstacles = [Obstacle() for _ in range(3)]  # Création ici de trois obstacles
            score.scorereset()  # Réinitialisation du score
        else:
            pygame.display.set_caption("Jeu")  # Changement du titre de la fenêtre en "Jeu"
            player.draw(screen)  # Affiche le joueur
            new_obstacles = []  # Création d'une nouvelle liste pour stocker les obstacles mis à jour


            # Boucle pour chaque obstacle
            for obstacle in obstacles:
                obstacle.draw(screen)  # Affichage de l'obstacle
                obstacle.deplacer()  # Déplacement de l'obstacle

                # Vérification de la position de l'obstacle
                if obstacle.rect.x <= -100:
                    new_obstacles.append(Obstacle())  # Création d'un nouvel obstacle si l'ancien est sorti de l'écran
                    score.scoreaug()  # Augmentation du score en cas de passage d'un obstacle
                else:
                    new_obstacles.append(obstacle)  # Conservation de l'obstacle existant

            obstacles = new_obstacles  # Mise à jour de la liste d'obstacles

            score.init_score_surface()  # Initialisation de la surface du score
            score.draw_score(screen)  # Affichage du score
            accueil.bouton_accueil()  # Affichage du bouton pour retourner à l'accueil

            # Vérification de la collision avec chaque obstacle
            for obstacle in obstacles:
                if player.mario_rect.colliderect(obstacle.rect):
                    pygame.mixer.music.load('images/Mario Death.mp3')
                    pygame.mixer.music.play(0)
                    accueil.gamerun = False  # Arrêt du jeu en cas de collision avec un obstacle
                    break

            player.update(input)  # Mise à jour de la position du joueur en fonction de la saisie de toute à l'heure
            player.decor()  # Affichage des éléments déco

        temps.tick(60)  # Limite le nombre d'images par seconde à 60
        pygame.display.update() # Actualise la page
        pygame.display.flip()

