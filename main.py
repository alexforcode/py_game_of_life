import pygame as pg

from data.game import Game


def start():
    pg.init()

    game = Game('Conway\'s Game of Life')
    game.start()

    pg.quit()


if __name__ == '__main__':
    start()