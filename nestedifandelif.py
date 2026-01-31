
# learning if nested if and elif

# if and elif ladder

temp = float(input("enter the temperature: "))

if temp == 25:
    print('Normal')
elif temp <25:
    print("cold")
elif temp > 25 :
    print("Hot")
else:
    print("entered value is not correct ")


# coding challange for Generate discount bill

Amount = int(input("Enter the amount:"))

if Amount < 1000:
    total = Amount - Amount * 0.10
    print("you will get 10% discount", total)

elif Amount >= 1000 and Amount < 5000:
    total = Amount - Amount * 0.15
    print("you will get 15% discount", total)

elif Amount >= 5000 and Amount < 10000:
    total = Amount - Amount * 0.20
    print("you will get 20% discount", total)

elif Amount >= 10000 and Amount < 500000:
    total = Amount - Amount * 0.25
    print("you will get 25% discount", total)

else:
    total = Amount - Amount * 0.30
    print("you will get 30% discount", total)



#challanges using nested if

daynumber = int(input("enter the day: "))

if daynumber == 0:
    print("Mon")
elif daynumber == 1:
    print("Tue")
elif daynumber == 2:
    print("Wed")
elif daynumber == 3:
    print("Thur")
elif daynumber == 4:
    print("Fri")
elif daynumber == 5:
    print("Sat")
elif daynumber == 6:
    print("Sun")
else:
    print("Please enter a valid input")


#month no to name

EnterMonthnumber = int(input("Enter the month number: "))

if EnterMonthnumber == 0:
    print("January")
elif EnterMonthnumber == 1:
    print("February")
elif EnterMonthnumber == 2:
    print("March")
elif EnterMonthnumber == 3:
    print("April")
elif EnterMonthnumber == 4:
    print("May")
elif EnterMonthnumber == 5:
    print("June")
elif EnterMonthnumber == 6:
    print("July")
elif EnterMonthnumber == 7:
    print("August")
elif EnterMonthnumber == 8:
    print("September")
elif EnterMonthnumber == 9:
    print("October")
elif EnterMonthnumber == 10:
    print("November")
elif EnterMonthnumber == 11:
    print("December")
else:
    print("Please enter a valid month number")


#convert digits to words

digittowords = int(input("Enter the number of digits: "))

if digittowords == 0:
    print("Zero")
elif digittowords == 1:
    print("One")
elif digittowords == 2:
    print("Two")
elif digittowords == 3:
    print("Three")
elif digittowords == 4:
    print("Four")
elif digittowords == 5:
    print("Five")
elif digittowords == 6:
    print("Six")
elif digittowords == 7:
    print("Seven")
elif digittowords == 8:
    print("Eight")
elif digittowords == 9:
    print("Nine")
elif digittowords == 10:
    print("Ten")
else:
    print("Enter the correct number")

