maths_mark = 999
english_mark = 999
ict_mark = 999

while (maths_mark < 0 or maths_mark >100):
    maths_mark = int(input("enter maths mark(0-100): "))
while (english_mark < 0 or english_mark >100):
    english_mark = int(input("enter english mark(0-100): "))
while (ict_mark < 0 or ict_mark >100):
    ict_mark = int(input("enter ict mark(0-100): "))

average_mark = (maths_mark + english_mark + ict_mark) /3

if average_mark >= 65:
    result = "pass"
else:
    result = "fail"

print(f"Average mark: {average_mark}: {result}")
