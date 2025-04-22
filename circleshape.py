import pygame

class CircleShape(pygame.sprite.Sprite):
    """
    A reusable base class for circular objects in the game.
    Handles position, velocity, radius, and basic collision logic.
    Inherits from pygame.sprite.Sprite for sprite group management.
    """
    def __init__(self, x, y, radius):
        """
        Initialize the circle shape with position, velocity, and radius.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
            radius (float): Radius of the circle.
        """
        # Automatically add to sprite group if 'containers' is defined
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def collides_with(self, other):
        """
        Check if this object collides with another circular object.

        Args:
            other (CircleShape): Another circular object.

        Returns:
            bool: True if the circles overlap, False otherwise.
        """
        distance = pygame.math.Vector2.distance_to(self.position, other.position)
        return distance <= self.radius + other.radius

    def draw(self, screen):
        """
        Placeholder method for drawing the object.
        Subclasses should override this method.

        Args:
            screen (Surface): Pygame surface to draw on.
        """
        pass

    def update(self, dt):
        """
        Placeholder method for updating the object state.
        Subclasses should override this method.

        Args:
            dt (float): Time delta since the last frame.
        """
        pass
