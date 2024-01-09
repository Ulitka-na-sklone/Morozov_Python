import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        matrix = [[0] * self.rows for i in range(self.cols)]
        if randomize:
            for i in range(self.cols):
                for j in range(self.rows):
                    matrix[i][j] = random.randint(0, 1)
        return matrix

    def get_neighbours(self, cell: Cell) -> Cells:
        a = cell[1]
        b = cell[0]
        Cells = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if 0 <= a + j < len(self.curr_generation[0]) and 0 <= b + i < len(self.curr_generation):
                        Cells.append(self.curr_generation[b + i][a + j])
        return Cells

    def get_next_generation(self) -> Grid:
        matrix = [[0] * self.rows for i in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = self.get_neighbours((i, j))
                if self.curr_generation[i][j] == 1 and 2 <= neighbours.count(1) <= 3:
                    matrix[i][j] = 1
                elif self.curr_generation[i][j] == 0 and neighbours.count(1) == 3:
                    matrix[i][j] = 1
        self.prev_generation = self.curr_generation
        self.curr_generation = matrix
        return matrix

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations == self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation != self.prev_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        new_grid = []
        with open(filename) as file:
            for i in file:
                new_grid.append([int(j) for j in i if (j == "0" or j == "1")])
        new_game = GameOfLife((len(new_grid), len(new_grid[0])))
        new_game.curr_generation = new_grid
        return new_game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as file:
            for i in range(self.rows):
                for j in range(self.cols):
                    file.write(str(self.curr_generation[i][j]))
                file.write("\n")