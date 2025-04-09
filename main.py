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
p1Score = 0
p2Score = 0

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
    ballSpeed = font.render(f"Velocity: {ball.velocity}",True,"cyan")
    score = font.render(f"{p1Score}:{p2Score}",True,"cyan")

    screen.fill('black')
    screen.blit(fpsCounter, (30,550))
    screen.blit(ballSpeed, (150,550))
    screen.blit(score, ((width-score.get_width())/2,50))
    keys = pygame.key.get_pressed()

    paddle1.draw(screen)
    paddle1.move(keys, pygame.K_w, pygame.K_s, height)

    paddle2.draw(screen)
    paddle2.move(keys, pygame.K_UP, pygame.K_DOWN, height)

    screen.blit(goalP1, goalP1Rect)
    screen.blit(goalP2, goalP2Rect)

    ball.draw(screen)
    ball.move(keys, pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l)


    # if (paddle1.rectangle).colliderect(ball.rectangle):
    #     print("paddle1 collided w ball")
    # if (paddle2.rectangle).colliderect(ball.rectangle):
    #     print("paddle2 collided w ball")
    ball.checkPaddleCollision([paddle1.rectangle,paddle2.rectangle],width,height)

    whoGoal = ball.checkGoalCollision([goalP1Rect,goalP2Rect],width,height)
    if whoGoal == 1:
        p1Score += 1
    if whoGoal == 2:
        p2Score += 1

    pygame.display.update()
    clock.tick(60)