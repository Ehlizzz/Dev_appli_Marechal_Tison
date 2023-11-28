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
        self.player = Player(self)
        self.all_players.add(self.player)

        #Group d'obstacles
        self.all_obstacles = pygame.sprite.Group()


        self.pressed = {}

    def start(self):
        self.jeustarting = True
        self.spawn_obstacle()

    def game_over(self):
        self.all_obstacles = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.rect.y = 500

        self.jeustarting = False
    def update(self, screen):
        # aplliquer le joueur
        screen.blit(self.player.image, self.player.rect)

        # Verifier si le joueur saute
        if self.pressed.get(pygame.K_UP):
            self.player.sauter()

        # Recuperer les obstacles
        for obstacles in self.all_obstacles:
            obstacles.deplacer()

        # regarde les collisions
        self.player.collision()

        # appliquer les obstacles
        self.all_obstacles.draw(screen)


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_obstacle(self):
        obstacle = Obstacle(self)
        self.all_obstacles.add(obstacle)