num = int(input("insert number "))

factorial = 1
while num > 1:
    factorial *= num # 5*1= 5, 5*4 =20, 20*3=60, 60*2=120
    num -= 1
print("factorial: ", factorial)
   
