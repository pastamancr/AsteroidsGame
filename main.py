import pygame
<<<<<<< HEAD
from constants.py import SCREEN_WIDTH, SCREEN_HEIGHT
=======
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
>>>>>>> d6f3c37 (added constants.py and added example print statements in the main.py file)


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
