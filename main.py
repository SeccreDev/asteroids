import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    """
    Main game loop for the Asteroids game.
    Sets up the game window, initializes game objects, and handles updates and rendering.
    """
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame and create the game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0

    # Sprite groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign sprite containers to respective classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    # Initialize player and asteroid field
    p1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    running = True
    while running:
        # Handle events (keyboard)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a color to wipe away anything from last frame. It clears the screen
        screen.fill("black")

        # Update all updatable game objects
        updatable.update(delta_time)

        # Handle collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(p1):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        # Draw all drawable game objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Limit FPS to 60. An calculates delta_time, which is used for framerate-independent physics
        delta_time = clock.tick(60) / 1000

    # Quit the game
    pygame.quit()
    
if __name__ == "__main__":
    main()
