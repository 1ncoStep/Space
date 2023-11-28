import random
import pygame as pg


class Spaceship(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load('Spaceship-PNG-File.png')
        self.image = pg.transform.scale(self.image, (200, 200))

        self.rect = self.image.get_rect()
        self.rect.center = (375, 800)

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.rect.x -= 3

        if keys[pg.K_d]:
            self.rect.x += 3

        if keys[pg.K_w]:
            self.rect.y -= 3

        if keys[pg.K_s]:
            self.rect.y += 3

    def resize(self):
        self.image = pg.transform.scale(self.image, (400, 500))

    def show_coords(self):
        return self.rect.center


class TestObjects(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.star = pg.image.load('звезда.png')
        self.star = pg.transform.scale(self.star, (20, 20))
        self.strect = self.star.get_rect()
        self.strect.x = random.randint(0, 750)
        self.strect.y = random.randint(0, 1000)

    def update(self):
        if random.randint(0, 1) == 0:
            self.strect.x += 1

        else:
            self.strect.x -= 1

        if random.randint(0, 1) == 0:
            self.strect.y += 1

        else:
            self.strect.y -= 1
