import pygame
from paddle import Paddle

width = 800
height = 600

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pingpong")
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)

paddleP = Paddle(-90,-90)
paddle1 = Paddle((0+60),(height/2)-paddleP.height/2)
paddle2 = Paddle((width-60-paddleP.width),(height/2)-paddleP.height/2)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    fps = clock.get_fps()
    font_surface = font.render(f"FPS: {fps:.2f} ",True,"cyan")

    screen.fill('black')
    screen.blit(font_surface, (30,550))
    keys = pygame.key.get_pressed()

    paddle1.draw(screen)
    paddle1.move(keys, pygame.K_w, pygame.K_s)

    paddle2.draw(screen)
    paddle2.move(keys, pygame.K_UP, pygame.K_DOWN)

    pygame.display.update()
    clock.tick(60)