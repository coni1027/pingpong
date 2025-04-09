import pygame

class Ball():
    def __init__(self, x, y, radius=14, color="white"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.surface = pygame.Surface((radius*2,radius*2))
        self.rectangle = self.surface.get_rect(center=(x,y))
        self.center = (self.radius,self.radius)
        self.speed = 8
        pygame.draw.circle(self.surface,self.color,self.center,self.radius)
    
    def move(self, keylist, upkey, downkey, leftkey, rightkey):
        if keylist[upkey]:
            self.rectangle.y -= self.speed
        if keylist[downkey]:
            self.rectangle.y += self.speed
        if keylist[leftkey]:
            self.rectangle.x -= self.speed
        if keylist[rightkey]:
            self.rectangle.x += self.speed

    def draw(self, screen):
        screen.blit(self.surface,self.rectangle)

    def resetPos(self, screen_width, screen_height):
        self.rectangle.center = (screen_width/2, screen_height/2)