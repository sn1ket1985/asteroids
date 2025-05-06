#Open the project folder in VSCode.
#Press Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (macOS).
#Type Python: Select Interpreter.
#Select the interpreter for the virtual environment (venv) that corresponds to the current project.



import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Window close clicked")
                return
            
            elif event.type == pygame.KEYDOWN:
                print(f"Key pressed: {pygame.key.name(event.key)}")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse clicked at {event.pos}")
        screen.fill("black")
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
    
   