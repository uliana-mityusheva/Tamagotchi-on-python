from tamagotchi import Print


class Command:
    def read_name(self):
        name = input()
        return name

    def choose_food(self):
        food = input()
        return food.lower()

    def choose_toy(self):
        toy = input()
        return toy.lower()

    def read(self, pet):
        command = input()

        if command.lower() == "parameters":
            pet.print_parameters()
        elif command.lower() == "feed":
            pet.feed()
        elif command.lower() == "play":
            pet.play()
        elif command.lower() == "sleep":
            pet.sleep()
        elif command.lower() == "treatment":
            pet.treatment()
        elif command.lower() == "sport":
            pet.sport()
        elif command.lower() == "toilet":
            pet.go_toilet()
        elif command.lower() == "exit":
            return 'exit'
        elif command.lower() == "help":
            _print = Print.Print()
            _print.help()
        else:
            _print = Print.Print()
            _print.error()

        return 'ok'
