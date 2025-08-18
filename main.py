import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    print("Starting Asteroids!")
    print(
f"Screen width: {SCREEN_WIDTH}\n"
f"Screen height: {SCREEN_HEIGHT}"
    )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
        


if __name__ == "__main__":
    main()
