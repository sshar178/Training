import Critter


def main():
    type = input("Beep or Boop? ")
    if type == 'Beep':
        bob = Critter.beep()
    elif type == 'Boop':
        bob = Critter.boop()
    bob.name = input('Name your critter! ')
    
    while bob.isAlive():
        action = input('What would you like ' + bob.name + ' to do? ')
        if action == 'eat':
            bob.feed()
            bob.Noise()
        elif action == 'sleep':
            bob.sleep()
            bob.Noise()
        elif action == 'workout':
            bob.workout()
            bob.Noise()
    print(bob.name +  ' has died.')

if __name__ == '__main__':
    main()
