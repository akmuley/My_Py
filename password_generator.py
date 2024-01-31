import random
def generate_password(len_of_pwd,upper_case_flag,dig_flag,spec_char):
    print(f"Values of all flags are - ", [len_of_pwd],[upper_case_flag],[dig_flag],[spec_char])

    len_of_pwd=int(len_of_pwd)
    print(len_of_pwd)
    letter_upper= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter_lower= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    special_char= ['!','@','#','$','%','&','*','^','|','_','+','(',')']
    Digit_list= [0,1,2,3,4,5,6,7,8,9]
    pass_list=[]
    pass_generated=""

    if upper_case_flag == 'y' and dig_flag == 'y' and spec_char == 'y':
        pass_list = letter_upper  + letter_lower + special_char + Digit_list
        for char in random.choices(pass_list,k=len_of_pwd):
            pass_generated = pass_generated + str(char)
        return(pass_generated)

    elif upper_case_flag == 'y' and dig_flag == 'y' and spec_char == 'n':
        pass_list = letter_upper + letter_lower + Digit_list
        for char in random.choices(pass_list,k=len_of_pwd):
            pass_generated = pass_generated + str(char)
        return(pass_generated)

    elif upper_case_flag == 'y' and dig_flag == 'n' and spec_char == 'y':
        #print("upper and spec")
        pass_list = letter_upper + letter_lower + special_char
        for char in random.choices(pass_list,k=len_of_pwd):
            pass_generated = pass_generated + str(char)
        return(pass_generated)

    elif upper_case_flag == 'y' and dig_flag == 'n' and spec_char == 'n':
        print("only upper ")
        pass_list = letter_upper + letter_lower
        for char in random.choices(pass_list,k=len_of_pwd):
            pass_generated = pass_generated + str(char)
        return(pass_generated)

    elif upper_case_flag == 'n' and dig_flag == 'y' and spec_char == 'y':
        print("dig and spec")
        pass_list = Digit_list + special_char + letter_lower
        for char in random.choices(pass_list,k=len_of_pwd):
            pass_generated = pass_generated + str(char)
        return(pass_generated)

    elif upper_case_flag == 'n' and dig_flag == 'y' and spec_char == 'n':
        print("only dig")
        pass_list = letter_lower + Digit_list
        for char in random.choices(pass_list,k=len_of_pwd):
            pass_generated = pass_generated + str(char)
        return(pass_generated)

    elif upper_case_flag == 'n' and dig_flag == 'n' and spec_char == 'y':
        print("only spec")
        pass_list = letter_lower + special_char
        for char in random.choices(pass_list,k=len_of_pwd):
            pass_generated = pass_generated + str(char)
        return(pass_generated)

    else:
        print("\nPlease retry as all N selected .!!")



choice = "Running"
while choice == "Running":
    print("\n********* Password Generator *********")
    print("--------------------------------------")
    print("Please choose Option below -->")
    print("1. Generate Password ")
    print("2. exit the program")

    a = int(input("Enter you option - "))
    if a == 2:
        choice = "Exit"
    if a == 1:
        len_of_pwd = int(input(" How Many Characters ? - "))

        upper_case_flag = str(input(" Use Upper Case  (y/n) ? - "))
        upper_case_flag=upper_case_flag.lower()

        dig_flag = str(input(" Use Digits (y/n) ? - "))
        dig_flag = dig_flag.lower()

        spec_char = str(input(" Use Special Characters (y/n) ? - "))
        spec_char = spec_char.lower()

        print(f"\nPassword Generated is -",generate_password(len_of_pwd, upper_case_flag, dig_flag, spec_char))



    else:
        print("Please enter correct value .!! ")

print("\nThanks for Using password generator, Enjoy your day ..!!! ")
