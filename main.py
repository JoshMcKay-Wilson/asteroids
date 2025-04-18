# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

        updatable.update(dt)
        player.shot_timer -= dt

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()



if __name__ == "__main__":
    main()

