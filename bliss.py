# bliss
# edit code and text - blissfully
# extensible, modulable code editor with an emphasis on productivity and looks
# this project follows the ti* philosophy: small, very extensible, doesn't compromise looks for usability and vice versa

import os
from rich import print
from sys import argv
command_line_arguments = argv[1:]
import pygame

if not os.path.isdir('tifer'):
    print('[red]tifer not installed, exiting[/red]')
    print('To install tifer, run [blue]git clone https://github.com/rexxt/tifer.git[/blue].')
    exit(1)

# from tifer.tifer import FileEditor

def main():
    pygame.init()

    font = pygame.font.SysFont(None, 20)

    project = ''
    if len(command_line_arguments) > 0:
        project = command_line_arguments.pop()

    pygame.display.set_caption("bliss - " + "no project" if project == '' else project)
    logo = pygame.image.load("icon.png")
    pygame.display.set_icon(logo)

    screen = pygame.display.set_mode((640,360), pygame.RESIZABLE)

    running = True
    while running:
        screen.fill((0,0,0))
        
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        img = font.render('hello', True, (255,255,255))
        screen.blit(img, (50, 50))
        
        pygame.display.flip()
        
     
if __name__=="__main__":
    main()