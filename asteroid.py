import pygame
from constants import LINE_WIDTH
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen):
            pygame.draw.circle(screen, color="white", center=self.position,
                               width=LINE_WIDTH, radius=self.radius)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        

