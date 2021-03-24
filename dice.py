import random

class Dice:
    def __init__(self):
        self.history = []
    def roll(self):
        r = random.randrange(6)+1
        self.history.append(r)
        return r

if __name__ == "__main__": #tests
    dice = Dice()
    print(dice.roll())
    print(dice.roll())
    print(dice.roll())
    print(dice.history)
