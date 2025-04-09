import pygame
from paddle import Paddle
from ball import Ball

width = 800
height = 600

pygame.init()
pygame.display.set_caption("Pingpong")

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)

paddleP = Paddle(-90,-90)
paddle1 = Paddle((0+60),(height/2)-paddleP.height/2)
paddle2 = Paddle((width-60-paddleP.width),(height/2)-paddleP.height/2)

goalP1 = pygame.Surface((8,height))
goalP1Rect = goalP1.get_rect()
goalP1.fill("red")

goalP2 = pygame.Surface((8,height))
goalP2Rect = goalP2.get_rect(topleft=(width-8,0))
goalP2.fill("red")

ball = Ball(500,500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    fps = clock.get_fps()
    fpsCounter = font.render(f"FPS: {fps:.2f} ",True,"cyan")
    ballSpeed = font.render(f"Speed: {ball.speed:.2f}",False,"cyan")

    screen.fill('black')
    screen.blit(fpsCounter, (30,550))
    screen.blit(ballSpeed, (150,550))
    keys = pygame.key.get_pressed()

    paddle1.draw(screen)
    paddle1.move(keys, pygame.K_w, pygame.K_s)

    paddle2.draw(screen)
    paddle2.move(keys, pygame.K_UP, pygame.K_DOWN)

    screen.blit(goalP1, goalP1Rect)
    screen.blit(goalP2, goalP2Rect)

    ball.draw(screen)
    ball.move(keys, pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l)


    if goalP1Rect.colliderect(ball.rectangle):
        print("p1 hit")
        ball.resetPos(width,height)
    if goalP2Rect.colliderect(ball.rectangle):
        print("p2 hit")
        ball.resetPos(width,height)

    pygame.display.update()
    clock.tick(60)