#Open the project folder in VSCode.
#Press Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (macOS).
#Type Python: Select Interpreter.
#Select the interpreter for the virtual environment (venv) that corresponds to the current project.



import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    
  
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
             
        pygame.display.flip()
        
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
    
   