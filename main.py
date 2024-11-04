import pygame
import random
pygame.init()

screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("my first game screen")

while True:
    color=(random.randint(0,100),random.randint(0,240),random.randint(0,255))
    color1=(random.randint(0,255),random.randint(0,100),random.randint(0,200))
    color2=(random.randint(0,55),random.randint(0,140),random.randint(0,150))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()

    screen.fill((255,255,255))
    pygame.draw.rect(screen,color,(150,230,100,100))
    pygame.time.delay(800)
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Hello, world!", True, (255, 0, 0))
    screen.blit(text_surface, (50, 50))

    pygame.display.flip()



