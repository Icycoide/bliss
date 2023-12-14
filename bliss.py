# bliss
# edit code and text - blissfully
# extensible, modulable code editor with an emphasis on productivity and looks
# this project follows the ti* philosophy: small, very extensible, doesn't compromise looks for usability and vice versa

import os
from rich import print
from sys import argv
command_line_arguments = argv[1:]
import pygame
import tools
import json
ui_config = json.load(open('UI.json'))

bliss_version = '0.1.1'

if not os.path.isdir('tifer'):
    print('[red]tifer not installed, exiting[/red]')
    print('To install tifer, run [blue]git clone https://github.com/rexxt/tifer.git[/blue].')
    exit(1)

# from tifer.tifer import FileEditor

def main():
    pygame.init()

    interface_font = pygame.font.SysFont(ui_config['interface_font'][0], ui_config['interface_font'][1])
    interface_font_bold = pygame.font.SysFont(ui_config['interface_font'][0], ui_config['interface_font'][1], bold=True)

    project = ''
    if len(command_line_arguments) > 0:
        project = command_line_arguments.pop()

    pygame.display.set_caption("Bliss - " + ("no project" if project == '' else project))
    logo = pygame.image.load("icon.png")
    pygame.display.set_icon(logo)

    screen = pygame.display.set_mode((640,360), pygame.RESIZABLE)

    keys = []
    running = True
    while running:
        screen.fill(ui_config['application_background'])
        

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN:
                keys.append(str(event.scancode))
            elif event.type == pygame.KEYUP:
                keys.remove(str(event.scancode))

        w, h = pygame.display.get_surface().get_size()
        status_bar_pos = tools.Point((0, h-ui_config['interface_font'][1]*2))
        pygame.draw.rect(screen, ui_config['status_bar_background'], pygame.Rect(status_bar_pos[0], status_bar_pos[1], w, ui_config['interface_font'][1]*2))
        tools.write_to_screen(screen, interface_font_bold, 'Bliss ' + bliss_version, status_bar_pos + tools.Point((ui_config['interface_font'][1]/2, ui_config['interface_font'][1]/2)), (True, ui_config['status_bar_foreground']))
        if len(keys) > 0:
            tools.write_to_screen(screen, interface_font_bold, ' '.join(keys), status_bar_pos + tools.Point((ui_config['interface_font'][1]/2 + 100, ui_config['interface_font'][1]/2)), (True, ui_config['status_bar_foreground']))
        
        pygame.display.flip()

if __name__=="__main__":
    main()