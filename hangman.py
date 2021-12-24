import random

#a
f = open('words.txt', "r")
words = f.readline().strip().split('"')
words = list(filter(lambda arg: arg != "" and arg != ',', words))
f.close()

#b
word = random.choice(words)
saved_word = word

#c
tmp_list = []
for _ in range(len(word)):
    print("_ ", end="")
    tmp_list.append("_")
print()


#d
fails = 0
used_letters = {""}
game = True
while game:
    letter = input()
    if letter == "":
        print("not a valid input")
    elif letter in used_letters:
        print(f"{letter} is already used")
    else:
        used_letters.add(letter)
        if letter in word:
            index = word.find(letter)
            while index != -1:
                tmp_list[index] = letter
                word = word.replace(letter, '_', 1)
                index = word.find(letter)
            print("".join(tmp_list))
        else:
            fails += 1
            if fails == 8:
                print(f"FAILED, THE WORD WAS: {saved_word}")
                game = False
            else:
                print(f"fails: {fails}/8")

        if "_" not in tmp_list:
            print(f"YOU WON! the word was {saved_word}")
            game = False