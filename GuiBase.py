import pygame


class TextElement(pygame.font.Font):

        def __init__(self, text = 'Default', size = '12', position = (0,0)):

            self.text = text
            self.size = size
            self.position = position




class VisualElement(pygame.sprite.DirtySprite):
    """ The Class for most GUI elements.
    x, y, width, height = int
    colour = tuple(int, int, int)
    """

    def __init__(self, x, y, width, height, colour):

        pygame.sprite.DirtySprite.__init__(self)
        self.width = width
        self.height = height
        self.colour = colour
        self.text = TextElement()

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def highlight(self):
        highlighted= [x+50 for x in self.colour if x < 225]
        self.image.fill(highlighted)

    def lowlight(self):
        lowlighted = [x-50 for x in self.colour if x > 30]
        self.image.fill(lowlighted)

    def render_text(self, text, position = False):
        if position:
            self.text.position = position
        else:
            self.text.position = (0,0)

        self.text.text = text
        font_object = pygame.font.Font( 'font1.ttf', 35)
        rendered_text = font_object.render(self.text.text, False, ((0,0,0)))
        self.image.blit(rendered_text, self.text.position)


    def fade_in(self):
        pass

    def fade_out(self):
        pass


class ClickableElement(VisualElement):
    """ Class made for mouse interaction such as button """


    def __init__(self, x, y, width, height, colour):
        VisualElement.__init__(self, x,y, width, height, colour)

    def on_hover(self, function, *args):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            function(*args)
        else:
            self.image.fill(self.colour)

    def on_click(self, function):
        pass

