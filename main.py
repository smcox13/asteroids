import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)    

    p1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    astroid_field1 = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for i in updatable:
            i.update(dt)
        
        for a in asteroids:
            if a.check_collision(p1):
                print("Game over!")
                exit()
            for s in shots:
                if s.check_collision(a):
                    s.kill()
                    a.split()

        screen.fill("black")

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()