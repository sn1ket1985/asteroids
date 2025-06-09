#Open the project folder in VSCode.
#Press Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (macOS).
#Type Python: Select Interpreter.
#Select the interpreter for the virtual environment (venv) that corresponds to the current project.



import pygame
import sys
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    dt = 0
    
  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:  # tryck på ESC
            pygame.quit()
            sys.exit()
        
        updatable.update(dt)
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
            
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    print("KILL")
                    asteroid.kill()
        pygame.display.flip()

        
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
    
   