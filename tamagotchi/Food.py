import abc
from abc import ABC


class Food(ABC):
    @abc.abstractmethod
    def health_change(self, min_, max_):
        pass

    @abc.abstractmethod
    def happiness_change(self, min_, max_):
        pass

    @abc.abstractmethod
    def need_go_toilet_change(self, min_, max_):
        pass

    @abc.abstractmethod
    def force_change(self, min_, max_):
        pass

    @abc.abstractmethod
    def satiety_change(self, min_, max_):
        pass


class Apple(Food):
    def health_change(self, min_, max_):
        return 1 * max_ // 10

    def happiness_change(self, min_, max_):
        return 1 * max_ // 10

    def need_go_toilet_change(self, min_, max_):
        return 1 * max_ // 10

    def force_change(self, min_, max_):
        return min_

    def satiety_change(self, min_, max_):
        return 1 * max_ // 10


class Salad(Food):
    def health_change(self, min_, max_):
        return 2 * max_ // 10

    def happiness_change(self, min_, max_):
        return 2 * max_ // 10

    def need_go_toilet_change(self, min_, max_):
        return 2 * max_ // 10

    def force_change(self, min_, max_):
        return 2 * max_ // 10

    def satiety_change(self, min_, max_):
        return 3 * max_ // 10


class Poke(Food):
    def health_change(self, min_, max_):
        return 4 * max_ // 10

    def happiness_change(self, min_, max_):
        return 2 * max_ // 10

    def need_go_toilet_change(self, min_, max_):
        return 3 * max_ // 10

    def force_change(self, min_, max_):
        return 4 * max_ // 10

    def satiety_change(self, min_, max_):
        return 5 * max_ // 10


class Chips(Food):
    def health_change(self, min_, max_):
        return -2 * max_ // 10

    def happiness_change(self, min_, max_):
        return 3 * max_ // 10

    def need_go_toilet_change(self, min_, max_):
        return 3 * max_ // 10

    def force_change(self, min_, max_):
        return 1 * max_ // 10

    def satiety_change(self, min_, max_):
        return 2 * max_ // 10


class Pancake(Food):
    def health_change(self, min_, max_):
        return -1 * max_ // 10

    def happiness_change(self, min_, max_):
        return 3 * max_ // 10

    def need_go_toilet_change(self, min_, max_):
        return 2 * max_ // 10

    def force_change(self, min_, max_):
        return 2 * max_ // 10

    def satiety_change(self, min_, max_):
        return 2 * max_ // 10


class Hamburger(Food):
    def health_change(self, min_, max_):
        return -4 * max_ // 10

    def happiness_change(self, min_, max_):
        return 5 * max_ // 10

    def need_go_toilet_change(self, min_, max_):
        return 5 * max_ // 10

    def force_change(self, min_, max_):
        return 6 * max_ // 10

    def satiety_change(self, min_, max_):
        return 8 * max_ // 10
