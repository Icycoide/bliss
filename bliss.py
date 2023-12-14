# bliss
# edit code and text - blissfully
# extensible, modulable code editor with an emphasis on productivity and looks
# this project follows the ti* philosophy: small, very extensible, doesn't compromise looks for usability and vice versa

import os
from rich import print
import pygame

if not os.path.isdir('tifer'):
    print('[red]tifer not installed, exiting[/red]')
    print('To install tifer, run [blue]git clone https://github.com/rexxt/tifer.git[/blue].')
    exit(1)

# from tifer.tifer import FileEditor
