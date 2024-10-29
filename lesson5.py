# IF STATEMENTS
# store data list, tuple, dictionary, set
# loops

# capture student's marks

entered_value = input("Enter your score:")
print(type(entered_value))

score = int(entered_value)  #int() convert to an integer

if entered_value.isnumeric() != True:
    print("Please enter a valid number")
    exit(0) #stop the program

if score >= 78:
    print("A")
elif score >= 71 and score <= 77:
    print("A-")
elif score >= 64 and score <= 70:
    print("B+")
elif score >= 57 and score <= 63:
    print("B")
elif score >= 50 and score <= 56:
    print("B-")
elif score >= 43 and score <= 49:
    print("C+")
else:
    print("C")

