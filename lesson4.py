# math functionality
import math

x = 99

square_root = math.sqrt(x)

print("Root is ", square_root)

rounded = round(square_root, 2)
print("Rounded to two decimal places ", rounded)

#Functions
# print(rounded)
print('--------------------------------------------------------')
# #calling a function
# print(round(6.549844984, 3))


y = 52.5894941
print(y)
print('--------------------------------------------------------')
print(round(y, 2))

print('--------------------------------------------------------')
name = "Rose Mary Jane"
print(len(name))
print(name.lower())
print(name.upper())
print(name.capitalize())  #capitalize the first name only
print(name.title())       #capitalize all names

print('--------------------------------------------------------')
message = 'This thing is so easy and fluent'
new_message = message.replace("fluent", "flowing")
print(new_message)