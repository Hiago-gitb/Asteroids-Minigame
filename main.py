import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys

def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0.0
    clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(x, y)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill("black")
        dt = clock.tick(60)/1000
        for thing in drawable:
            thing.draw(screen)
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
    
main()
