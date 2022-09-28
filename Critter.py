from logging import exception
#import time
#class Food:
#    def eat(self):
#        raise exception
#class choccy(Food):
#    x = 1
#    y = 1
#
#class apple(Food):
#    x = 2
#    y = 2

#class pizza(Food):
#    x = 3
#    y = 3
        
class Critter:
    __isAlive = True
    __foodLevel = 5
    __tiredness = 0
    __fitness = 5
    name = ""

    def isAlive(self):
        return self.__isAlive

    def __die(self):
        self.__isAlive = False


    def sleep(self):
        print(self.name + ' is sleeping.')
        print('Zzzzz')
        time.sleep(5)
        print(self.name + ' is awake')
        self.__tiredness = 0
        self.__foodLevel -= 2
        if (self.__foodLevel <= 0):
            print(self.name +  ' starved to death.')
            self.__die()

    def feed(self):
        if self.__isAlive:
        #    x,y = 0
        #    eat = input("what you wanna eat? choccy(c), apple(a), pizz(p)")
        #    if eat == 'c':
        #        x = choccy.x
        #        y = choccy.y
        #    elif eat =='a':
        #        x = apple.x
        #        y = apple.y
        #    elif eat == 'p':
        #        x = pizza.x
        #        y = pizza.y
            print(self.name + ' is eating.')
            print("Nom nom nom")
            self.__foodLevel += 2
            self.__tiredness += 2
            if self.__foodLevel > 10:
                print(self.name + ' over ate')
                self.__die()
            elif self.__tiredness > 5:
                print(self.name + ' is sleepy from so much food.')
                self.sleep()
    
    def workout(self):
        if self.__isAlive:
            print(self.name + ' pumping iron BABYYYYy')
            print('AAAAAAAAAAAA')
            self.__foodLevel -= 2
            self.__tiredness += 2
            self.__fitness += 2
            if self.__foodLevel < 0:
                print(self.name + ' clearly didnt have his pre workout and died')
                self.__die()
            if self.__tiredness > 5:
                print(self.name + ' passed out in the gym')
                self.sleep()
            if self.__fitness >=10 :
                print('Congratulations! ' + self.name + ' is a Greek god of a critter')
                exit(0)

class beep(Critter):
    def Noise(self):
        print('Beep Beep')

class boop(Critter):
    def Noise(self):
        print('Boop Boop')




