import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        p1.update(dt)

        screen.fill("black")
        p1.draw(screen)
        pygame.display.flip()

        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()