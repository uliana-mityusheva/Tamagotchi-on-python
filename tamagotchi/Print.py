class Print:
    __zero = "| | | | | | | | | | |"
    __one = "|*| | | | | | | | | |"
    __two = "|*|*| | | | | | | | |"
    __three = "|*|*|*| | | | | | | |"
    __four = "|*|*|*|*| | | | | | |"
    __five = "|*|*|*|*|*| | | | | |"
    __six = "|*|*|*|*|*|*| | | | |"
    __seven = "|*|*|*|*|*|*|*| | | |"
    __eight = "|*|*|*|*|*|*|*|*| | |"
    __nine = "|*|*|*|*|*|*|*|*|*| |"
    __ten = "|*|*|*|*|*|*|*|*|*|*|"

    __help = """You can use these commands to take care of your pet:
- sleep
- feed
- sport
- play
- feed
- toilet
- treatment
- parameters (to view all the pet's life parameters)
- exit (to finish the game)"""

    def hello(self):
        print("Hello, let's start the game!\nCome up with a name for your pet")

    def start(self, name):
        print("Ok, now you can play with " + name)

    def choose_food(self, name):
        print("Choose meal for " + name)
        print("apple\tpoke\tpancake\tchips\tsalad\thamburger")

    def choose_toy(self, name):
        print("Choose toy for " + name)
        print("ball\tcomputer\tpuzzle")

    def error(self):
        print("Wrong command")

    def print_parameter(self, parameter, max_):
        if parameter == 0 * max_ // 10:
            return self.__zero
        elif parameter == 1 * max_ // 10:
            return self.__one
        elif parameter == 2 * max_ // 10:
            return self.__two
        elif parameter == 3 * max_ // 10:
            return self.__three
        elif parameter == 4 * max_ // 10:
            return self.__four
        elif parameter == 5 * max_ // 10:
            return self.__five
        elif parameter == 6 * max_ // 10:
            return self.__six
        elif parameter == 7 * max_ // 10:
            return self.__seven
        elif parameter == 8 * max_ // 10:
            return self.__eight
        elif parameter == 9 * max_ // 10:
            return self.__nine
        else:
            return self.__ten

    def print_force(self, force, max_):
        print("{:<13}".format("force:") + self.print_parameter(force, max_))

    def print_happiness(self, happiness, max_):
        print("{:<13}".format("happiness:") + self.print_parameter(happiness, max_))

    def print_health(self, health, max_):
        print("{:<13}".format("health:") + self.print_parameter(health, max_))

    def print_sleep(self, sleep, max_):
        print("{:<13}".format("sleep:") + self.print_parameter(sleep, max_))

    def print_need_toilet(self, need_toilet, max_):
        print("{:<13}".format("need_toilet:") + self.print_parameter(need_toilet, max_))

    def print_satiety(self, satiety, max_):
        print("{:<13}".format("satiety:") + self.print_parameter(satiety, max_))

    def go_sleep(self, name):
        print(name + " slept")

    def sport(self, name):
        print(name + " did some sports")

    def force_to_sport(self, name):
        print(name + " need more forces to sport")

    def toilet(self, name):
        print(name + " went to the toilet")

    def treatment(self, name):
        print(name + " recovered")

    def end(self):
        print("Thanks for playing!")

    def sick(self, name):
        print(name + " is sick")

    def boring(self, name):
        print(name + " is boring")

    def need_toilet(self, name):
        print(name + " needs to go to the toilet")

    def hungry(self, name):
        print(name + " is hungry")

    def sleep(self, name):
        print(name + " wants to sleep")

    def tired(self, name):
        print(name + " is tired")

    def force_to_treatment(self, name):
        print(name + " need more forces to treatment")

    def sleep_to_treatment(self, name):
        print(name + " need more sleep to treatment")

    def salad(self, name):
        print(name + " ate the salad")

    def hamburger(self, name):
        print(name + " ate the hamburger")

    def pancake(self, name):
        print(name + " ate the pancake")

    def apple(self, name):
        print(name + " ate the apple")

    def chips(self, name):
        print(name + " ate the chips")

    def poke(self, name):
        print(name + " ate the poke")

    def ball(self, name):
        print(name + " played a ball")

    def computer(self, name):
        print(name + " played a computer game")

    def puzzle(self, name):
        print(name + " played a puzzle")

    def died(self, name):
        print(name + " is died :(")

    def help(self):
        print(self.__help)
