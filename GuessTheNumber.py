import random
def game(num=0,start=0,end=100):
    if num == 0:
        num = random.randrange(start, end)
    g = True
    while g:
        inp = int(input("Enter a guess:\n"))
        if inp > num:
            print("too high")
        elif inp < num:
            print("too low")
        else:
            print("Found number!")
            g = False

if __name__ == "__main__":
    game(5)
