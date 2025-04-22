import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    """
    Represents an asteroid object in the game. Inherits from CircleShape to handle
    position, radius, and collision.
    """
    def __init__(self, x, y, radius):
        """
        Initialize an asteroid with position (x, y) and a given radius.
        """
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        """
        Draw the asteroid as a white outline circle on the screen.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        """
        Update the asteroid's position based on its velocity and the time delta.

        Args:
            dt (float): Time passed since the last update.
        """
        self.position += self.velocity * dt
    
    def split(self):
        """
        Split the asteroid into two smaller asteroids if it's above the minimum radius.
        The original asteroid is removed.
        """
        self.kill()  # Remove the current asteroid from the game

        # If the asteroid radius is below the minimum radius it won't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        
        # Randomize the angle of the split
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        # Create two smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
