import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    """
    Represents a projectile shot by the player.
    Inherits from CircleShape to include position, velocity, and radius.
    """
    def __init__(self, x, y):
        """
        Initialize the shot with its position and radius.

        Args:
            x (float): Initial x-coordinate of the shot.
            y (float): Initial y-coordinate of the shot.
        """
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """
        Draw the shot as a circle on the screen.

        Args:
            screen (Surface): Pygame surface to draw on.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """
        Update the position of the shot based on its velocity.

        Args:
            dt (float): Time delta since the last frame.
        """
        self.position += self.velocity * dt