from tamagotchi import MyPet
from tamagotchi import Print
from tamagotchi import Command
import time


print_ = Print.Print()
print_.hello()

pet = MyPet.MyPet()
command = Command.Command()

pet.name = command.read_name()
print_.start(pet.name)

pet.status = 'ok'
read = 'ok'

timing = time.time()

while read != 'exit' and pet.status != 'died':
    read = command.read(pet)
    pet.status = pet.check_status()

    if time.time() - timing > 15:
        interval = (time.time() - timing) // 15
        pet.check_alive(interval)
        timing = time.time()

if pet.status == 'died':
    print_.died(pet.name)

status = 'exit'

print_.end()
