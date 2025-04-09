import pygame
import random

class Ball():
    def __init__(self, x:int, y:int, radius=14, color="white"):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.surface = pygame.Surface((radius*2,radius*2))
        self.rectangle = self.surface.get_rect(center=(x,y))
        self.center = (self.radius,self.radius)
        self.velocity = pygame.Vector2(5*random.choice([-1,1]),5*random.choice([-1,1]))
        pygame.draw.circle(self.surface,self.color,self.center,self.radius)
    
    def move(self, keylist:list, upkey, downkey, leftkey, rightkey):
        if keylist[upkey]:
            self.rectangle.y -= self.velocity.y
        if keylist[downkey]:
            self.rectangle.y += self.velocity.y
        if keylist[leftkey]:
            self.rectangle.x -= self.velocity.x
        if keylist[rightkey]:
            self.rectangle.x += self.velocity.x

    def draw(self, screen):
        screen.blit(self.surface,self.rectangle)

    def resetPos(self, screenWidth, screenHeight):
        self.rectangle.center = (screenWidth/2, screenHeight/2)

    def update(self, screenWidth:int, screenHeight:int):
        if self.rectangle.top <= 0 or self.rectangle.bottom >= screenHeight:
            self.velocity.y *= -1
        self.rectangle.x += self.velocity.x
        self.rectangle.y += self.velocity.y        
    
    def checkGoalCollision(self,goalRects:list,screenWidth:int,screenHeight:int):
        for goalRect in goalRects:
            if self.rectangle.colliderect(goalRect) and goalRect.x > screenWidth // 2:
                print(f"P1 goal")
                self.resetPos(screenWidth, screenHeight)
                self.velocity = pygame.Vector2(5*random.choice([-1,1]),5*random.choice([-1,1]))
                return 1
            if self.rectangle.colliderect(goalRect) and goalRect.x < screenWidth // 2:
                print(f"P2 goal")
                self.resetPos(screenWidth, screenHeight)
                self.velocity = pygame.Vector2(5*random.choice([-1,1]),5*random.choice([-1,1]))
                return 2
        return 0
    
    def checkPaddleCollision(self,paddleRects:list,screenWidth:int,screenHeight:int):
        for paddleRect in paddleRects:
            if self.rectangle.colliderect(paddleRect) and paddleRect.x < screenWidth // 2:
                print("collided with p1")
                self.velocity.x *= -1
            if self.rectangle.colliderect(paddleRect) and paddleRect.x > screenWidth // 2:
                print("collided with p2")
                self.velocity.x *= -1