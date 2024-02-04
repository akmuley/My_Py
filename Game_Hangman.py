
#This code includes only logic no graphics, game is incomplete 
import random
a = ["beekeeper", "war","dogcarer","foodlover"]

choose= random.choice(a)
print("Word is -",choose)
length_of_word= len(choose)
#print(length_of_word)
a = []
for i in range(length_of_word):
    a.append("_")

print(a)

end_of_game=0
lives = 4

while end_of_game == 0:
    guess = input("Guess the word - ")

    if guess not in choose:
        print("Wrong")
        lives -=1
        if lives == 0:
            print("You Lost All lives , you loose")
            end_of_game=1
    else:
        print("right")
        for i in range(length_of_word):
            letter = choose[i]
            if guess == letter:
                a[i]=guess
        print(a)
        if "_" not in a:
            print("You Won")
            end_of_game = 1

print(a)
