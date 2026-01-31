# check  leap year

# what is leap year
# it is a special year and a year has 29 days in feb it is called as leap year

year = int(input("enter the year: "))

if year % 100 == 0:
    if year % 400 == 0:
     print("leap year")
    else:
     print("not leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not leap year")

