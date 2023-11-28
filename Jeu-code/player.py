import pygame


#Creer une classe qui va etre le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load("Assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.y = 500

    def sauter(self):
        if not self.game.check_collision(self, self.game.all_obstacles):
            self.rect.y -= self.velocity

    def collision(self):
        if self.game.check_collision(self, self.game.all_obstacles):
            self.game.game_over()
