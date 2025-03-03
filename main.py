import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    Player1 = Player(x = SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Player1.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))
        Player1.draw(screen)
        dt = clock.tick(60)/1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
