import MyPet
import Print
import Command

print_ = Print.Print()
print_.hello()

pet = MyPet.MyPet()
command = Command.Command()

pet.name = command.read_name()
print_.start(pet.name)

status = 'ok'
read = 'ok'

while read != 'exit' and status != 'died':
    read = command.read(pet)
    status = pet.check_alive()

if status == 'died':
    print_.died(pet.name)

print_.end()
