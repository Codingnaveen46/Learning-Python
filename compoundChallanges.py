
#challanges for solving vowel and consants

#Aeiou  vowels


letter = input("Enter a letter: ")

if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U' :

    print("vowels")
else:
    print("consonants")


# exam  result

# maths physics chem

# maxmarks = 100
# minmarks = 45


Maths = int(input("Enter a maths: "))
physics = int(input("Enter a physics: "))
chemistry = int(input("Enter a chemistry: "))

if Maths >= 45 and Maths <= 100 and physics >= 45 and physics <= 100 and chemistry >= 45 and chemistry <= 100:
    print("pass")
else:
    print("fail")

    #other method

if Maths >= 45 and physics >= 45 and chemistry >= 45:
    print("pass")
else:
    print("fail")
