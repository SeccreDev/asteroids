import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    running = True

    # Player Initialization
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        p1.update(delta_time)
        p1.draw(screen)
        # Flip the display to put your work on screen
        pygame.display.flip()

        # Limit FPS to 60. delta_time is used for framerate-independent physics
        delta_time = clock.tick(60) / 1000

    pygame.quit()
    
if __name__ == "__main__":
    main()
