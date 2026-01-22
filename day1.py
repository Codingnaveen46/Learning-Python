import sys

length = 15
print(type(length))

prices = [30,30,40,56]
print(prices)

name1, price, quantity = 'soap',23.7,6
print(name1, price, quantity)

a,b,c = 1,1,1
print(id(a),id(b),id(c))

a=b=c= 1
print(a,b,c)


#### python is dynamically typed language

#python and javascript




# What is statically typed language ?

# c,c++, java are statically typed language


flotvalue = 34.77
print(type(flotvalue))

onearry = [1,2,3,4,5]
print(type(onearry))




#Rules for variables names

#Name should be meaning full
# example
prod_id = 145
print(type(prod_id))

price = 23.4
print(type(price))

cust_name = 'smith'
print(cust_name)

cust_city = 'banalore'
print(cust_city)



# Alphanumeric and underscore

a1 = 10
cust_name = 'smith'
print(cust_name)
cust_city = 'banalore'
print(cust_city)

# cust-name = 'smith'  not allowed


# Must start with letter or underscore

address1 ='delhi'
print(address1)

#not allows 1address = 'delhi


# should not be a keyword

# 1 keywoard / reserve word
# 2 identifier



#case -sensetive



#Data types

#numeric
   # int , float, bool, complex

   #sequence
     # sequence type supports collections of values  and can be accessed by the index values
     # list =  l = [2,2,2,33,4,]  this is mutable
     # tuples = t = (98,4,4,5)  this is immutable
     # string =  it is a collection of characters  s = ' p y t h o n'  immutable


     #set
     # it is a collection of values [vector values] the data will not have the index and the data are unordered
      #s = {3,4,5,6,7}

s = {3,4,4,5,6,5,}
print(s)


#dictionary

#dict it is collection of (key, value)  this is mutable



dect = {'name_1': 'prem', 'age_3': 22, 'dep_3': 'cse'}
print(dect.values())


s = "python programming"
print(s.__len__())
print(s.upper())
print(s.count('p'))
print(s.replace("python","java"))


student = {
    "name": "Naveen",
    "age": 22,
    "course": "CSE"
}

student.update({"city":"Bangalore"})
student.update({"age":"23"})
student.pop("course")

print(student)


#7th

myset = {1,2,3,4}
myset.add(5)
myset.remove(3)
myset.add(2)
print(myset)


#6th

tap_r = (2,3,4,5,6)
# tap_r[0] = 10
print(tap_r)

#5th

nums = [10, 20, 30, 40, 50,89]


print(nums.index(10))
print(nums.index(40))

nums.append(44)
nums.remove(20)

print(len(nums))
print(nums)

numstring = "25"

print(int(numstring))
print(float(numstring))
print(str(numstring))

bus = 'voluo'
car = 'maruthi'

bus, car = car,bus
print(bus, car)


 #input()
# print(type(input()))

li= [i for i in range(1,101)]
print(li[1:100:3])

#numeric types in python

# int flot bool complex type are the numeric data types

import sys

x = 12324747278827348237482734872842834243823878373874873874834
m = 101
print(id(m))
print(id(x))
y = 28947398749827348273984728974928748927487289748927948729878947273482734324
m = 205

print(m)
print(id(m))
print(sys.getsizeof(m))



arep = 125E2
print(arep)

arep1 = 2345E-2
print(arep1)



#float positive and negative

e = 29.67
f = -1.76
g = -2.5e2
h = -3.1e-2

print(e,f,g,h)


#learning bool and complex

#bool initilization and declaration

i = 10
j = 2

print( j > i )


k = True
L = False

print(int(k))

print(type(L))


c2 = 3+5j
print(type(c2))

c3 = complex(-1,-2)
print(type(c3))

c4 = complex(10)
print(c4)

