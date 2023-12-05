import pygame
import random
#Creer la class obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100

        self.image = pygame.image.load("Assets/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(100, 300)
        self.rect.y = 540
        self.velocity = 1

    def deplacer(self):
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.velocity
        if self.rect.x <= 0:
            self.rect.x = 2000
            self.health = 100
