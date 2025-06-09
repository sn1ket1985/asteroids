from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    
    def draw(self, screen):
     	pygame.draw.circle(screen, "blue",self.position,self.radius,2)
      
    def update(self, dt):
        self.position += self.velocity*dt