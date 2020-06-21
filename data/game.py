import pygame as pg
from pygame.locals import *

from .constants import *


class Game(object):
    def __init__(self, caption):
        self._caption = caption or DEFAULT_CAPTION
        pg.display.set_caption(self._caption)
        self._screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self._clock = pg.time.Clock()
        self._stop = False

    def _event_handler(self):
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self._stop = True

            if event.type == QUIT:
                self._stop = True

    def start(self):
        while not self._stop:
            self._clock.tick(FPS)
            self._screen.fill(WHITE)
            self._event_handler()
            pg.display.update()
