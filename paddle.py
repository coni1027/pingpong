import pygame

class Paddle:
    def __init__(self, x, y, width=15, height=90, color="cyan"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.Surface((width,height))
        self.rectangle = self.surface.get_rect(topleft=(x,y))
        self.surface.fill(color)
        self.speed = 8

    def move(self, keylist, upkey, downkey, screenHeight):
        if keylist[upkey] and self.rectangle.top > 0:
            self.rectangle.y -= self.speed
        if keylist[downkey] and self.rectangle.bottom < screenHeight:
            self.rectangle.y += self.speed

    def draw(self, screen):
        screen.blit(self.surface,self.rectangle)
    