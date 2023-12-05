import pygame


class Score:

    # Initialisation des scores et des éléments liés à l'affichage du texte
    def __init__(self):
        pygame.mixer.init()
        self.score = 0  # Score actuel du joueur
        self.high_score = 0  # Meilleur score atteint

        # Initialisation de la police et de la taille du texte
        self.police = pygame.font.Font(None, 36)

        # Création de la surface de texte pour le score
        self.texte_surface = self.police.render("Score : " + str(self.score), True, "black", "gray")

        # Position du texte pour le score
        self.texte_rect = self.texte_surface.get_rect()
        self.texte_rect.center = (1220, 75)

        # Création de la surface de texte pour le meilleur score
        self.texte_surface1 = self.police.render("High_Score : " + str(self.high_score), True, "black", "gray")

        # Position du texte pour le meilleur score
        self.texte_rect1 = self.texte_surface1.get_rect()
        self.texte_rect1.center = (1187, 108)

    # Initialisation des surfaces de texte pour le score et le meilleur score
    def init_score_surface(self):
        self.texte_surface = self.police.render("Score : " + str(self.score), True, "black", "gray")
        self.texte_surface1 = self.police.render("High_Score : " + str(self.high_score), True, "black", "gray")

    # Affichage du score et du meilleur score à l'écran
    def draw_score(self, screen):
        screen.blit(self.texte_surface, self.texte_rect)
        self.texte_rect1.center = (1187, 108)
        screen.blit(self.texte_surface1, self.texte_rect1)

    # Affichage du meilleur score avec effet clignotant
    def draw_score_high(self, screen):
        self.texte_rect1.center = (1280 / 2, 720 / 2)

        # Utilisation d'un chronomètre pour alterner entre les couleurs
        time = pygame.time.get_ticks()

        # Changement de couleur toutes les 1000 millisecondes (1 seconde)
        if time % 1000 < 250:
            couleur_texte = "red"
        else:
            couleur_texte = "dark red"

        # Rendu du texte avec la couleur déterminée
        self.texte_surface1 = self.police.render("High_Score : " + str(self.high_score), True, couleur_texte)
        screen.blit(self.texte_surface1, self.texte_rect1)

    # Augmentation du score et mise à jour de l'affichage
    def scoreaug(self):
        self.score += 1
        self.update()

    # Réinitialisation du score
    def scorereset(self):
        self.score = 0

    # Mise à jour du meilleur score si le score actuel est supérieur
    def update(self):
        if self.score  == self.high_score:
            pygame.mixer.music.load('images/super-mario-bros-coin.mp3')
            pygame.mixer.music.play(0)

        if self.high_score < self.score:
            self.high_score = self.score


