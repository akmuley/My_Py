#This is a Bill splitter application , which takes bill amount , tip percent , no of people as input and genrates share of each


print("******************** Welcome To Bill Splitter ********************")

bill_amount = float(input("Please Enter the bill amount = "))
tip_percent = float(input("Please Enter tip percent = "))
no_of_people = int(input("Total Number of Guest = "))
#print(f"Bill amount is -",bill_amount)
#print("Tip percent - ",tip_percent)
#print("Total Number of Guest - ",no_of_people)
share = ((bill_amount + (bill_amount*tip_percent)/100))/no_of_people
print("*********************************************************")
print(f"Each Person will pay £{share}")
