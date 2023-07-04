#if, elifs, else statements 
#conditionals statements are used to accomadate different paths our code can follow
#if statements when a specific condition is met

my_bool = True

if my_bool:
    print("my bool is true")
else:
    print("my is false")

    #Nested if statements

#if some_condition:
#    if some other condition:
#        .....
#    else:
#        ....
#else:
#   ......

# Conditionals

# equals to: == 
# not equal to: !=
# less than: <
# more than: >
# less than or equal to: <=/>=


# Examples

money = 9

if money > 10:
    print("I have alot")
else:
    print("I'm broke")

#elif - else if 
# We dont always need to check if every statement evaluates to true
# mostly only one statement will be true
# elif makes our code more efficiant
# Will only run if no other statement has been evaluated as true

temp = 40

if temp >= 30:
    print("its very hot")
elif temp > 25:
    print("its pretty hot")
elif temp > 20:
    print("it's ok")
elif temp > 14:
    print("could be better")
elif temp == 0:
    print("freezing")
else:
    print("normally bad")

# Exercise
# Ask for an input form a user for a grade/mark
# if the mark is greater than 85 print "distinction"
# if the mark is between 65 and 85 print "pass"
# anything else print "fail"
# DO this with just if statements first, then with elif statememts 


if x >= 85:
    print: