import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):

    shot_timer = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_timer <= 0:
            self.shoot(SHOT_RADIUS, self.position)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, radius, position):
        shot = Shot(position.x, position.y, radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        print(f"Shot fired!")




