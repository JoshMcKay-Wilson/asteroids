import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius,):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", [self.position.x, self.position.y], self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            ast_1_velocity = self.velocity.rotate(angle)
            ast_2_velocity = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            #pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = ast_1_velocity
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = ast_2_velocity
            #asteroid = Asteroid(position.x, position.y, radius)




        


