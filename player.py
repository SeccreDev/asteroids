import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    """
    Represents the player-controlled spaceship.
    Inherits from CircleShape and adds rotation, shooting, and movement.
    """
    def __init__(self, x, y):
        """
        Initialize the player with position, rotation, and shoot cooldown.

        Args:
            x (float): Initial x-coordinate.
            y (float): Initial y-coordinate.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
    
    def draw(self, screen):
        """
        Draw the player as a triangle on the screen.

        Args:
            screen (Surface): Pygame surface to draw on.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def triangle(self):
        """
        Calculate the vertices of the triangular ship based on rotation.

        Returns:
            list[Vector2]: List of three points representing the triangle.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        """
        Rotate the player ship.

        Args:
            dt (float): Time delta to scale the rotation.
        """
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        """
        Move the player forward or backward.

        Args:
            dt (float): Time delta to scale the movement direction and speed.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        """
        Fire a projectile if the cooldown has elapsed.
        """
        if self.shoot_timer > 0:
            return None
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        """
        Update player state based on input and cooldowns.

        Args:
            dt (float): Time delta since the last frame.
        """
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


