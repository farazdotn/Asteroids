import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    print(
f"Screen width: {SCREEN_WIDTH}\n"
f"Screen height: {SCREEN_HEIGHT}"
    )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        for asteroid in asteroids:
            if player.Collision(asteroid):
                sys.exit("Game over!")

    pygame.quit()


if __name__ == "__main__":
    main()
