import pygame

WHITE = (225, 225, 225)


class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # this is passing the color and the x, y of the walls
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # now initialise the attributes of the wall
        self.width = width
        self.height = height
        self.color = color
        # draw the walls for
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

        self.rect = self.image.get_rect()
