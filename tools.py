def write_to_screen(screen, font, text, pos, flags):
    img = font.render(text, *flags)
    screen.blit(img, pos)

class Point(tuple):
    def __add__(self, other):
        if isinstance(other, tuple):
            return Point((self[0] + other[0], self[1] + other[1]))
    def __sub__(self, other):
        if isinstance(other, tuple):
            return Point((self[0] - other[0], self[1] - other[1]))