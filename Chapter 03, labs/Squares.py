num = 1
while num <= 100:
    square = num**2
    if square > 2000:
        break
    print(num, "=", square)
    num += 1