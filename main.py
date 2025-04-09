import pygame
from paddle import Paddle
from ball import Ball

"""CONSTANTS"""
WIDTH = 900 
HEIGHT = 600
PADDLE_SPEED = 8
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
PADDLE_OFFSET = 60
GOAL_WIDTH = 8
BALL_SPEED_INCREMENT = 0.8
PADDLE_SPEED_INCREMENT = 0.4
SPEEDUP_INTERVAL = 3000  # in millisecond

def drawHUD():
    fps = clock.get_fps()
    fpsCounter = font.render(f"FPS: {fps:.2f} ",True,"cyan")
    ballSpeed = font.render(f"BVelocity: {ball.velocity}",True,"cyan")
    paddle1Speed = font.render(f"P1Speed: {paddle1.speed:.2f}",True,"cyan")
    paddle2Speed = font.render(f"P2Speed: {paddle1.speed:.2f}",True,"cyan")

    screen.blit(fpsCounter, (30,520))
    screen.blit(ballSpeed, (30,550))
    screen.blit(paddle1Speed, (150,520))
    screen.blit(paddle2Speed, (300,520))
    
pygame.init()
pygame.display.set_caption("Pingpong")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)
p1Score,p2Score = 0,0

paddle1 = Paddle((0+PADDLE_OFFSET),(HEIGHT/2)-PADDLE_HEIGHT/2)
paddle2 = Paddle((WIDTH-PADDLE_OFFSET-PADDLE_WIDTH),(HEIGHT/2)-PADDLE_HEIGHT/2)

goalP1 = pygame.Surface((GOAL_WIDTH,HEIGHT))
goalP1Rect = goalP1.get_rect()
goalP1.fill("red")

goalP2 = pygame.Surface((GOAL_WIDTH,HEIGHT))
goalP2Rect = goalP2.get_rect(topleft=(WIDTH-GOAL_WIDTH,0))
goalP2.fill("red")

ball = Ball(WIDTH/2,HEIGHT/2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    extra = font.render("SCORE",True,"cyan")
    score = font.render(f"{p1Score}:{p2Score}",True,"cyan")

    screen.fill('black')
    screen.blit(extra, ((WIDTH-extra.get_width())/2,30))
    screen.blit(score, ((WIDTH-score.get_width())/2,50))

    # for debugging
    # drawHUD()

    keys = pygame.key.get_pressed()

    paddle1.draw(screen)
    paddle1.move(keys, pygame.K_w, pygame.K_s, HEIGHT)

    paddle2.draw(screen)
    paddle2.move(keys, pygame.K_UP, pygame.K_DOWN, HEIGHT)

    screen.blit(goalP1, goalP1Rect)
    screen.blit(goalP2, goalP2Rect)

    ball.draw(screen)
    ball.update(WIDTH,HEIGHT)
    ball.checkPaddleCollision([paddle1.rectangle,paddle2.rectangle],WIDTH,HEIGHT)
    
    whoGoal = ball.checkGoalCollision([goalP1Rect,goalP2Rect],WIDTH,HEIGHT)
    if whoGoal == 1:
        showScore = font.render("Player 1 Scored!",True,"cyan")
        screen.blit(showScore,((WIDTH-showScore.get_width())/2,70))
        p1Score += 1
        paddle1.speed = PADDLE_SPEED
        paddle2.speed = PADDLE_SPEED
        pygame.display.update()
        pygame.time.delay(1000)
    if whoGoal == 2:
        showScore = font.render("Player 2 Scored!",True,"cyan")
        screen.blit(showScore,((WIDTH-showScore.get_width())/2,70))
        p2Score += 1
        paddle1.speed = PADDLE_SPEED
        paddle2.speed = PADDLE_SPEED
        pygame.display.update()
        pygame.time.delay(1000)

    # scaling of game
    if pygame.time.get_ticks() % SPEEDUP_INTERVAL < 20:
        speed = ball.velocity.length()
        ball.velocity = ball.velocity.normalize() * (speed + BALL_SPEED_INCREMENT)
        paddle1.speed += PADDLE_SPEED_INCREMENT
        paddle2.speed += PADDLE_SPEED_INCREMENT

    pygame.display.update()
    clock.tick(60)