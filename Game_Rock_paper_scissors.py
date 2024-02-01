import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

a = 0

while a == 0:
    print("************************** Welcome To Rock Paper Scissors !! *************")
    user_choice = int(input(" Please select 1 for rock , 2 for paper , 3 for Scissors - "))

    if user_choice > 3:
        print("Wrong Input , Please select again .")
    else:
        if user_choice == 1:
            print("Your Choice -",rock)

        elif user_choice == 2:
            print("Your Choice -",paper)

        else:
            print("Your Choice -",scissors)
        choice = [1,2,3]
        computer_choice= random.choice(choice)

        if computer_choice == 1:
            print("Computer's choice -",rock)
        elif computer_choice == 2:
            print("Computer's choice -",paper)
        else:
            print("Computer's choice -",scissors)

        if user_choice == computer_choice:
            print("Its a Draw !")
        elif user_choice == 1 and computer_choice == 2:
            print("Computer Won !")
        elif user_choice == 1 and computer_choice == 3:
            print("You Won !")
        elif user_choice == 2 and computer_choice == 1:
            print("You Won !")
        elif user_choice == 2 and computer_choice == 3:
            print("Computer Won !")
        elif user_choice == 3 and computer_choice == 1:
            print("Computer Won !")
        else:
            print("You Won !")

        play_again = str(input("Play again (y or n) ? - ")).lower()
        print(play_again)
        if play_again == 'n':

            a += 1

print("Thanks for Playing  !!")
