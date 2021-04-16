from tamagotchi import Command
from tamagotchi import Food
from tamagotchi import Print
from tamagotchi import Toy


class MyPet:
    __max_status = 10
    __min_status = 0

    __health = __max_status
    __sleep = __max_status
    __need_toilet = __min_status
    __force = __max_status
    __satiety = __max_status
    __happiness = __max_status

    status = 'ok'

    def __check_status__(self, status):
        if status > self.__max_status:
            status = self.__max_status
        elif status < self.__min_status:
            status = self.__min_status
        return status

    name = "name"

    def print_parameters(self):
        print_ = Print.Print()

        print_.print_force(self.__force, self.__max_status)
        print_.print_happiness(self.__happiness, self.__max_status)
        print_.print_satiety(self.__satiety, self.__max_status)
        print_.print_health(self.__health, self.__max_status)
        print_.print_sleep(self.__sleep, self.__max_status)
        print_.print_need_toilet(self.__need_toilet, self.__max_status)

    def change_food(self, food):
        self.__happiness += food.happiness_change(self.__min_status, self.__max_status)
        self.__force += food.force_change(self.__min_status, self.__max_status)
        self.__satiety += food.satiety_change(self.__min_status, self.__max_status)
        self.__health += food.health_change(self.__min_status, self.__max_status)
        self.__need_toilet += food.need_go_toilet_change(self.__min_status, self.__max_status)

    def feed(self):
        print_ = Print.Print()

        print_.choose_food(self.name)

        command = Command.Command()
        ans = command.choose_food()
        if ans == "apple":
            apple = Food.Apple()
            self.change_food(apple)
            print_.apple(self.name)

        elif ans == "pancake":
            pancake = Food.Pancake()
            self.change_food(pancake)
            print_.pancake(self.name)

        elif ans == "hamburger":
            hamburger = Food.Hamburger()
            self.change_food(hamburger)
            print_.hamburger(self.name)

        elif ans == "chips":
            chips = Food.Chips()
            self.change_food(chips)
            print_.chips(self.name)

        elif ans == "poke":
            poke = Food.Poke()
            self.change_food(poke)
            print_.poke(self.name)

        elif ans == "salad":
            salad = Food.Salad()
            self.change_food(salad)
            print_.salad(self.name)

        else:
            print_.error()

        self.__happiness = self.__check_status__(self.__happiness)
        self.__force = self.__check_status__(self.__force)
        self.__satiety = self.__check_status__(self.__satiety)
        self.__health = self.__check_status__(self.__health)
        self.__need_toilet = self.__check_status__(self.__need_toilet)

    def change_toy(self, toy):
        self.__happiness += toy.happiness_change(self.__min_status, self.__max_status)
        self.__satiety += toy.satiety_change(self.__min_status, self.__max_status)
        self.__force += toy.force_change(self.__min_status, self.__max_status)
        self.__sleep += toy.sleep_change(self.__min_status, self.__max_status)

    def play(self):
        print_ = Print.Print()
        print_.choose_toy(self.name)

        command = Command.Command()
        ans = command.choose_toy()

        if ans == "ball":
            ball = Toy.Ball()
            self.__health += ball.healthy_change(self.__min_status, self.__max_status)
            self.change_toy(ball)
            print_.ball(self.name)

        elif ans == "computer":
            computer = Toy.ComputerGame()
            self.__health += computer.healthy_change(self.__min_status, self.__max_status)
            self.change_toy(computer)
            print_.computer(self.name)

        elif ans == "puzzle":
            puzzle = Toy.Puzzle()
            self.change_toy(puzzle)
            print_.puzzle(self.name)

        self.__happiness = self.__check_status__(self.__happiness)
        self.__force = self.__check_status__(self.__force)
        self.__satiety = self.__check_status__(self.__satiety)
        self.__health = self.__check_status__(self.__health)
        self.__sleep = self.__check_status__(self.__sleep)

    def sleep(self):
        self.__force += 5 * self.__max_status // 10
        self.__force = self.__check_status__(self.__force)

        self.__sleep = self.__max_status
        print_ = Print.Print()
        print_.go_sleep(self.name)

    def sport(self):
        print_ = Print.Print()
        if self.__force > 4 * self.__max_status // 10:
            self.__force += -4 * self.__max_status // 10
            self.__health += 4 * self.__max_status // 10
            self.__sleep += -3 * self.__max_status // 10
            self.__satiety += -3 * self.__max_status // 10

            self.__check_status__(self.__force)
            self.__check_status__(self.__satiety)
            self.__check_status__(self.__health)
            self.__check_status__(self.__sleep)

            print_.sport(self.name)
        else:
            print_.force_to_sport(self.name)

    def treatment(self):
        print_ = Print.Print()

        if self.__sleep > 3 * self.__max_status // 10 and self.__force > 2 * self.__max_status // 10:
            self.__health = self.__max_status
            print_.treatment(self.name)
        else:
            if self.__sleep <= 3 * self.__max_status // 10:
                print_.sleep_to_treatment(self.name)

            if self.__force <= 3 * self.__max_status // 10:
                print_.force_to_treatment(self.name)

    def go_toilet(self):
        self.__need_toilet = self.__min_status

        print_ = Print.Print()
        print_.toilet(self.name)

    def check_alive(self, interval):
        self.__happiness -= interval
        self.__health -= interval
        self.__satiety -= interval
        self.__sleep -= interval
        self.__need_toilet += interval

    def check_status(self):
        if self.__health == self.__min_status or self.__satiety == self.__min_status or \
                (self.__happiness == self.__min_status and self.__force == self.__min_status and
                 self.__sleep == self.__min_status):
            return "died"
        else:
            print_ = Print.Print()

            if self.__health < 3 * self.__max_status // 10:
                print_.sick(self.name)

            if self.__need_toilet > 8 * self.__max_status // 10:
                print_.need_toilet(self.name)

            if self.__happiness < 4 * self.__max_status // 10:
                print_.boring(self.name)

            if self.__satiety < 2 * self.__max_status // 10:
                print_.hungry(self.name)

            if self.__sleep < 3 * self.__max_status // 10:
                print_.sleep(self.name)

            if self.__force < 2 * self.__max_status // 10:
                print_.tired(self.name)

        return "ok"
