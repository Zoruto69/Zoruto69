import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((780, 560)) #you can change it

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60) #this as well, but not recomended

game.run()
