word = input("Enter a word: ")
vowels = "aeiou"
count = 0

for letter in word:
    if letter.lower() in vowels:
        count += 1

print("The number of vowels in the word is:", count)