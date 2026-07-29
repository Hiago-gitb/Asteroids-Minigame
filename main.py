import pygame
from constants import *
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0,0,0)
while True:
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    screen.fill("black")
    pygame.display.flip()
def main() -> None:
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
main()
