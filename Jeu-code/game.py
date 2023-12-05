import pygame.sprite

from player import Player
from obstacles import Obstacle

#creer un class game
class Game:
    def __init__(self):
        # jeu commencer ?
        self.jeustarting = False

        #generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player()
        self.all_players.add(self.player)

        #Group d'obstacles
        self.all_obstacles = pygame.sprite.Group()


        self.pressed = {}

    def start(self):
        self.jeustarting = True
        self.spawn_obstacle()

    def game_over(self):

        self.jeustarting = False
    def update(self, screen):
        # aplliquer le joueur
        self.player.update()
        # Verifier si le joueur saute
        if self.pressed.get(pygame.K_UP):
            self.player.saut()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_obstacle(self):
        obstacle = Obstacle(self)
        self.all_obstacles.add(obstacle)