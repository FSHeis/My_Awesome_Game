import random
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen):
            pygame.draw.circle(screen, color="white", center=self.position,
                               width=LINE_WIDTH, radius=self.radius)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, radius)
            asteroid1.velocity = velocity1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, radius)
            asteroid2.velocity = velocity2 * 1.2
        

