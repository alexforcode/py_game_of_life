from random import choice

import pygame as pg

from .constants import *


class Cell(object):
    def __init__(self, col, row):
        self._col = col
        self._row = row
        self._x = self._col * CELL_SIZE
        self._y = self._row * CELL_SIZE
        self._alive = False
        self._neighbours = []

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, flag):
        self._alive = flag

    @property
    def col(self):
        return self._col

    @property
    def row(self):
        return self._row

    @property
    def neighbours(self):
        return self._neighbours

    def get_alive_neighbours(self):
        count = 0
        for neighbour in self._neighbours:
            if neighbour.alive:
                count += 1

        return count

    def draw(self, screen):
        if self._alive:
            pg.draw.rect(screen, BLACK, (self._x, self._y, CELL_SIZE, CELL_SIZE))


class Grid(object):
    def __init__(self):
        self._cols = SCREEN_WIDTH // CELL_SIZE
        self._rows = SCREEN_HEIGHT // CELL_SIZE
        self._grid = []
        self._living_cells = []
        self._build_grid()

    def _neighbour_index(self, col, row):
        if col < 0:
            col = self._cols - 1
        elif col > self._cols - 1:
            col = 0
        if row < 0:
            row = self._rows - 1
        elif row > self._rows - 1:
            row = 0
        return col + row * self._cols

    def _add_neighbours(self, cell):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                index = self._neighbour_index(cell.col + i, cell.row + j)
                if index:
                    cell.neighbours.append(self._grid[index])

    def _build_grid(self):
        for row in range(self._rows):
            for col in range(self._cols):
                cell = Cell(col, row)
                cell.alive = choice((True, False))
                self._grid.append(cell)
                self._living_cells.append(cell.alive)

        for cell in self._grid:
            self._add_neighbours(cell)

    def _update(self):
        for i in range(len(self._grid)):
            liv_count = self._grid[i].get_alive_neighbours()
            if self._grid[i].alive and (liv_count < 2 or liv_count > 3):
                self._living_cells[i] = False
            elif not self._grid[i].alive and liv_count == 3:
                self._living_cells[i] = True

        for i in range(len(self._living_cells)):
            self._grid[i].alive = self._living_cells[i]

    def draw(self, screen):
        for cell in self._grid:
            cell.draw(screen)

        self._update()
