import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,screen):
        pygame.draw.circle(screen, "white",self.position, self.radius , width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        randomAngle = random.uniform(20,50)
        newAngleA = self.velocity.rotate(randomAngle)
        newAngleB = self.velocity.rotate(-randomAngle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS
        NewAsteroidA = Asteroid(self.position.x, self.position.y, newRadius)
        NewAsteroidA.velocity = newAngleA * 1.2
        NewAsteroidB = Asteroid(self.position.x, self.position.y, newRadius)
        NewAsteroidB.velocity = newAngleB * 1.2


