# Error handling

x = input("Your first number: ")
y = input("Your second number: ")
z = input("Your third number: ")

try:
    x_num = int(x)
    y_num = int(y)
    z_num = int(z)
    print(x_num * y_num * z_num)
except:
    print("Enter valid numbers")

