# learning literals in python

# Integer  flot boolean complex string

# what are literals  : the direct values which are used directly is called literals  also called as constants

#integer literals are the literals which contains the underscore for the values ex: a = 12_33_454_45


a = 23_234_342_34
print(type(a))
print(a)

#flot literals

a = 12_5.6_7
print(type(a))
print(a)

c = 13e2
print(type(c))
print(c)

d = 123e-2
print(type(d))
print(d)


#boolean literals


#complex literals

a = 4+5j
print(type(a))
print(a)

b = 1_3 + 2j
print(type(b))
print(b)


#string literals : a collection of characters which form a sentence or a word is called string

# string can be written in single ''   double ""   trible """ """"


name1 = 'naveen'
name2 = "naveen"
name3 = '''naveen'''
print(name1, name2, name3)



#integrer literals

# Decimal number    Binary number   octal number   Hexa number
   # a = 10          a = 0b1010      a = 0o12       a = 0xA


name4 = 10
name5 = 0b1010
name6 = 0o12
name7 = 0xA
print(name4, name5, name6, name7)
print(type(name5))



#base conversion functions

# python has the built in functions and also we can create our own functions


bin(123)
print(type(bin(123)))

oct(123)
print(type(oct(123)))

hex(123)
print(type(hex(123)))

s1 = bin(10)
print(type(s1))
print(s1)

s2 = oct(10)
print(type(s2))
print(s2)

s3 = hex(123)
print(type(s3))
print(s3)


s4 = bin(True)
print(type(s4))
print(s4)

# type conversion

# int can do conversion of flot ,boolen , string

a = 40.65
print(int(a))


b = True
print(int(b))

c = '344'
print(int(c))
print(type(int(c)))

# float

# it support all except the complex

a1 = 123
print(float(a1))

a2 = True
print(float(a2))

a3 = '12.75'
print(float(a3))


# bool function
# it works for all the data types

b1 = 1
print(bool(b1))
print(type(bool(b1)))

b2 = -12
print(bool(b2))
print(type(bool(b2)))

b3 = -1.2E-3
print(bool(b3))
print(type(bool(b3)))

b4 = 3+4j
print(bool(b4))
print(type(bool(b4)))

b5 = 'False'
print(bool(b5))
print(type(bool(b5)))

b6 = False
print(bool(b6))
print(type(bool(b6)))

b7 = ''
print(bool(b7))
print(type(bool(b7)))


#comlex

#suppoerts all the types

c1 = 10+3
print(complex(c1))
print(type(complex(c1)))


c2 = -12.5
print(complex(c2))
print(type(complex(c2)))


c3 = True
print(complex(c3))
print(type(complex(c3)))

c4 = False
print(complex(c4))
print(type(complex(c4)))


#String

#support all the data  types

d1 = 10
print(str(d1))
print(type(str(d1)))

d2 = -12
print(str(d2))
print(type(str(d2)))


d3 = -2.3E-3
print(str(d3))
print(type(str(d3)))

d4 = False
print(str(d4))
print(type(str(d4)))

d5 = 3+4j
print(str(d5))
print(type(str(d5)))


## learning operators

#1 arithmetic operators

# addition = + /operator

a = 10
b = 20
c = a + b

print(c)


#subtraction

a = 10
b = 20
c = a - b

print(c)


#multiplication

a = 10
b = 20
c = a * b

print(c)


# division

a = 10
b = 20
c = a / b

print(c)


#floor division and modulus

a = 14
b = 4

c = a // b
print(c)

c = a % b
print(c)

c = a /b
print(c)


# exponentiation(power)


c = 34 ** 4
print(c)


#  Expressions

# expressions are important

#expression
# precedence of operators   : operator has the precedence

#Associativity of operators
# importanance of parenthesis  execution will be done based on the pranthesis ( 2+5 )*(6-3) /2


e1 = ((5+3) * (5-3) //2)
print(e1)

##Taking input from the keyborad


length = int(input('Enter a length: '))
breadth = int(input('Enter a breadth: '))

area = length * breadth
print('area' , area )





























