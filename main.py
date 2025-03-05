import pygame
from constants import *
from player import Player,Shot
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containters = (updateable, drawable)
    NewField = AsteroidField()
    Player1 = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    gostatus = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))
        for draws in drawable:
            draws.draw(screen)
        for possible in asteroids:
            gostatus = Player1.collisionDetection(possible)
            if gostatus == True:
                print("Game Over!")
                pygame.quit()
                sys.exit()

        dt = clock.tick(60)/1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
