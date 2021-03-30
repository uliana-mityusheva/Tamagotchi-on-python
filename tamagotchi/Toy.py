import abc
from abc import ABC


class Toy(ABC):
    @abc.abstractmethod
    def happiness_change(self, min_, max_):
        pass

    @abc.abstractmethod
    def force_change(self, min_, max_):
        pass

    @abc.abstractmethod
    def satiety_change(self, min_, max_):
        pass

    @abc.abstractmethod
    def sleep_change(self, min_, max_):
        pass


class Ball(Toy):
    def happiness_change(self, min_, max_):
        return 4 * max_ // 10

    def force_change(self, min_, max_):
        return -5 * max_ // 10

    def satiety_change(self, min_, max_):
        return -3 * max_ // 10

    def sleep_change(self, min_, max_):
        return -3 * max_ // 10

    def healthy_change(self, min_, max_):
        return 2 * max_ // 10


class ComputerGame(Toy):
    def happiness_change(self, min_, max_):
        return 5 * max_ // 10

    def force_change(self, min_, max_):
        return -3 * max_ // 10

    def satiety_change(self, min_, max_):
        return -2 * max_ // 10

    def sleep_change(self, min_, max_):
        return -4 * max_ // 10

    def healthy_change(self, min_, max_):
        return -2 * max_ // 10


class Puzzle(Toy):
    def happiness_change(self, min_, max_):
        return 3 * max_ // 10

    def force_change(self, min_, max_):
        return -2 * max_ // 10

    def satiety_change(self, min_, max_):
        return -1 * max_ // 10

    def sleep_change(self, min_, max_):
        return -1 * max_ // 10
