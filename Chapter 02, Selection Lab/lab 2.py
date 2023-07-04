#task_1

age = int(input("enter age "))

if age >= 18:
    print("category A")
if age >= 16 and age < 18:
    print("category B")
if age < 16:
    print("category C")

#task 2

num1 = float (input("enter first number "))
num2 = float (input("enter second number "))

print("calculator options")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice = input("please choose option 1-4: ")
if choice == "1": # == is for comparing
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif choice == "2":                         #elif triggers when the if staement does not trigger or anything before it including elif statements
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif choice == "3":
    result = num1 * num2
    print(num1, "x", num2, "=", result)
elif choice == "4":
    if num2 == 0:
        print("Error: division by zero")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
else:
    print("Error: invalid choice")

#task 3

mark = int(input("mark: "))
level = int(input("Enter student level (1 or 2): "))

if mark < 1 or mark > 100:
    print("error must be between 1 and 100")
elif level == 1:
    if mark < 50:
        print("fail")
    elif mark <= 60:
        print("pass")
    elif mark <= 70:
        print("merit")
    else:
        print("Distinction")
elif level == 2:
    if mark < 40:
        print("Fail")
    elif mark <= 50:
        print("Pass")
    elif mark <= 65:
        print("Merit")
    else:
        print("Distinction")

else:
    print("invalid level must be 1 or 2")

#task 4 

print("1. side a")
print("2. side b")
print("3. side c")

choice = input("enter your choice: ")

if choice == "1":
    side_b = float(input("enter length of side b: "))
    side_c = float(input("enter length of side c: "))
    side_a = (side_c**2 - side_b**2)**0.5
    print("Length of side A is", side_a)
elif choice == "2":
    side_a = float(input("Enter length of side A: "))
    side_c = float(input("Enter length of side C: "))
    side_b = (side_c**2 - side_a**2)**0.5
    print("Length of side B is", side_b)
elif choice == "3":
    side_a = float(input("Enter length of side A: "))
    side_b = float(input("Enter length of side B: "))
    side_c = (side_a**2 + side_b**2)**0.5
    print("Length of side C is", side_c)
else:
    print("Invalid choice, please enter 1, 2, or 3.")