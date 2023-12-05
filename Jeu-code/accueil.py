import pygame

import game
from game import Game
class Accueil:
    def __init__(self, game):
        self.game = game
                                     # Créer la fenêtre du jeu
        pygame.init()
        # Taille de la fenêtre
        self.WIDTH, self.HEIGHT = 1280, 720
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Dimensions des cases
        self.CASE_WIDTH, self.CASE_HEIGHT = 200, 200

        # Combien de case par la couleur
        self.rect_colors = ['white', 'white']

        #Création bouton start
        self.rect_start = pygame.Rect((self.WIDTH / 2) - 150, 550, 300, 75)
        # Création bouton Menu
        self.rect_menu = pygame.Rect((self.WIDTH - 50), 0, 50, 25)

                                            # Création des rectangles

        self.rectangles = []

        nombre_rectangle = len(self.rect_colors)
        self.total_rect_width = nombre_rectangle * self.CASE_WIDTH

        # Définir l'espace entre les rectangles
        espace_rectangle = (self.WIDTH - self.total_rect_width) / (nombre_rectangle + 1)



        for i in range(nombre_rectangle):
            x = espace_rectangle * (i + 1) + i * self.CASE_WIDTH
            y = (self.HEIGHT - self.CASE_HEIGHT) / 2
            rect = pygame.Rect(x, y, self.CASE_WIDTH, self.CASE_HEIGHT)
            self.rectangles.append(rect)

        # Selection de base
        self.selection = 1
        self.windows = 0

        self.curseur = self.rectangles[1]

        self.font = pygame.font.Font(None,36)  # Utilise une police par défaut avec une taille de 36


    def bouton_selection(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Déplacer le selecteur et enregistre la selection de case
        for i, rect in enumerate(self.rectangles):
            if rect[0] + rect[2] > mouse[0] > rect[0] and rect[1] + rect[3] > mouse[1] > rect[1]:
                self.rect_colors[i] = 'yellow'
                if click[0] == 1:
                    self.selection = i
                    self.curseur = self.rectangles[i]

            else:
                self.rect_colors[i] = 'white'

    def bouton_accueil(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Bouton acceuil
        if (self.WIDTH) > mouse[0] > (self.WIDTH)-50 and 50 > mouse[1] > 0:
            pygame.draw.rect(self.SCREEN, 'yellow', self.rect_menu, 8)
            if click[0] == 1:
                self.windows = 0



    # Fonction qui gère le bouton start

    def bouton_start(self):
        #Récupérer la position de la souris
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Détection de la souris dans le rectangle du bouton
        if (self.WIDTH/2)-150 + 300 > mouse[0] > (self.WIDTH/2)-150 and 550+75 > mouse[1] > 550:
            pygame.draw.rect(self.SCREEN, 'yellow', self.rect_start, 7)
            if click[0] == 1:
                self.game.start()


    # Fonction qui gère l'affichage de l'accueil
    def show_accueil(self):
        self.SCREEN.fill('black')
        pygame.display.set_caption("Accueil")

        # Dessiner les rectangles
        for i, rect in enumerate(self.rectangles):
            pygame.draw.rect(self.SCREEN, self.rect_colors[i], rect, 5)

        # Dessiner le bouton start
        pygame.draw.rect(self.SCREEN, 'White', self.rect_start, 3)
        pygame.draw.rect(self.SCREEN, 'blue', self.curseur, 9)


