import pygame

# Définition de la classe Accueil
class Accueil:
    # Initialisation de la classe
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        # Définition de la taille de la fenêtre
        self.WIDTH, self.HEIGHT = 1280, 720
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Chargement de l'image de fond
        self.background = pygame.image.load('images/paysage_mario.png')

        # Définition des dimensions des cases et des couleurs des rectangles
        self.CASE_WIDTH, self.CASE_HEIGHT = 200, 200
        self.rect_colors = ['white', 'white']

        # Définition des rectangles pour les boutons
        self.rect_start = pygame.Rect((self.WIDTH / 2) - 150, 550, 300, 75)
        self.imagestart = pygame.image.load("images/start_icon.png")
        self.imagestart = pygame.transform.scale(self.imagestart, (self.rect_start[2], self.rect_start[3]))

        self.rect_menu = pygame.Rect((self.WIDTH - 60), 5, 60, 50)
        self.imageaccueil = pygame.image.load("images/accueil_icon.jpg.png")
        self.imageaccueil = pygame.transform.scale(self.imageaccueil, (self.rect_menu[2], self.rect_menu[3]))

        self.imagemario = pygame.image.load("images/mario_image_select.png")
        self.imagemario = pygame.transform.scale(self.imagemario, (self.CASE_WIDTH, self.CASE_HEIGHT))
        self.imageluigi = pygame.image.load("images/luigi_image_select.png")
        self.imageluigi = pygame.transform.scale(self.imageluigi, (self.CASE_WIDTH, self.CASE_HEIGHT))

        self.son = ['images/its-me-mario.mp3', 'images/luigi-its-me.mp3']


        # Création des rectangles pour la sélection du personnage
        self.rectangles = []

        nombre_rectangle = len(self.rect_colors)
        self.total_rect_width = nombre_rectangle * self.CASE_WIDTH

        # Définition de l'espace entre les rectangles
        espace_rectangle = (self.WIDTH - self.total_rect_width) / (nombre_rectangle + 1)

        for i in range(nombre_rectangle):
            x = espace_rectangle * (i + 1) + i * self.CASE_WIDTH
            y = (self.HEIGHT - self.CASE_HEIGHT) / 2
            rect = pygame.Rect(x, y, self.CASE_WIDTH, self.CASE_HEIGHT)
            self.rectangles.append(rect)

        # Initialisation des variables de sélection et d'état du jeu
        self.selection = 1
        self.windows = 0
        self.curseur = self.rectangles[1]
        self.font = pygame.font.Font(None, 36)
        self.gamerun = False

    # Gestion du survol et du clic sur les boutons de sélection du personnage
    def bouton_selection(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for i, rect in enumerate(self.rectangles):
            if rect.collidepoint(mouse):
                self.rect_colors[i] = 'yellow'
                if click[0] == 1:
                    self.selection = i
                    pygame.mixer.music.load(self.son[i])
                    pygame.mixer.music.play(0)
                    self.curseur = self.rectangles[i]
            else:
                self.rect_colors[i] = 'white'

    # Gestion du bouton de retour à l'écran d'accueil
    def bouton_accueil(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        self.SCREEN.blit(self.imageaccueil, self.rect_menu)

        if self.rect_menu.collidepoint(mouse):
            pygame.draw.rect(self.SCREEN, 'yellow', self.rect_menu, 8)
            if click[0] == 1:
                self.gamerun = False

    # Gestion du bouton de démarrage du jeu
    def bouton_start(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        self.SCREEN.blit(self.imagestart, self.rect_start)

        if self.rect_start.collidepoint(mouse):
            pygame.draw.rect(self.SCREEN, 'yellow', self.rect_start, 7, 10, 10, 10, 10)
            if click[0] == 1:
                self.gamerun = True

    # Affichage de l'écran d'accueil avec les personnages et les boutons
    def show_accueil(self, screen):
        screen.blit(self.background, (0, -80))
        pygame.display.set_caption("Accueil")

        # Affichage des rectangles de sélection
        [pygame.draw.rect(self.SCREEN, self.rect_colors[i], rect, 5) for i, rect in enumerate(self.rectangles)]

        # Affichage du cadre autour du bouton de démarrage
        pygame.draw.rect(self.SCREEN, 'White', self.rect_start, 5, 10, 10, 10, 10)

        # Affichage du curseur de sélection
        pygame.draw.rect(self.SCREEN, 'blue', self.curseur, 9)

        # Affichage des images des personnages
        self.SCREEN.blit(self.imagemario, self.rectangles[0].topleft)
        self.SCREEN.blit(self.imageluigi, self.rectangles[1].topleft)

    # Vérification de l'état du jeu (démarré ou arrêté)
    def verifrun(self):
        if self.gamerun:
            return 1
        else:
            return 0
