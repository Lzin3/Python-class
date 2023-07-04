# Different ways of storing data
# Lists - ordered, mutable, collection of values
# Dictionaries - unordered, mutable, collection of key-value pairs
# Tuple - ordered, immunatble, collection of values. 
# sets - unordered, mutable, collection of unique values.

#lists are stored in a variable []

colours = ["blue","red","yellow","pink"]

print (colours)

#referencing - elements in a list by the index position
#starts from position 0 going Backwards -1
#the index starts from position 0 

print(colours[0])
print(colours[3])

#slicing - create a sub - list up to the 2nd number but does not include the 2nd number
print(colours[0:2])
print(colours[:4])

#altering lists - use index position, need a value, delete with del button on key board

food = ["bread", "cheese", "pasta", "apple"]

food[0] = "rice"
del food[1]
#del food deletes one food from the list
print (food)

#checking if item in a list

print("pasta" in food)
print("orange" in food)
#it will print true or false depending if the fruit is in the list

#nested listed
numbers = [1, 2, 3, 4]
letters = ["a", "b", "c","d"]

combined = [numbers, letters]

print(combined[0][2], combined[1][3])  #the [0] in the index represents the 1st lidt which would be the numbers list and the [1] is letters

# multiple data types
my_list = ["red", 5, ["green", "apple"], 10.5] #talk to chris about it

print(my_list)
print(my_list[2][1])
print(my_list[0])

#list methods

#appends
my_fruits = ["apple","orange", "kiwi"]
my_fruits.append("pear")
print(my_fruits)

# Remove

 
my_fruits.remove("apple")
print(my_fruits)

# Insert

my_fruits.insert(0, "mango")
my_fruits.insert(1, "melon")
print(my_fruits)

# Extend with a list

my_fruits.extend(["grape", "cherry"])
print(my_fruits)

# Finding index position

print(my_fruits.index("orange"))

# Reversing a list

my_fruits.reverse()
print(my_fruits)

# Sorting

my_fruits.sort()
print(my_fruits)

my_fruits.sort(key=len) #(key=len) this sorts the list from shortest word to longst word on the list
print(my_fruits)

#join

x = ", ".join(my_fruits)
print(x)

#dicitonaires {} key:values pairs
#similar to a list, no indexing
#keys have to have unique values

drinks = {"fizzy": "sprite", "still": "water", "juice":"orange", "alcoholic":"beer"}
print(drinks)
print(drinks["fizzy"])

#adding dictionary

drinks["non-alcoholic"] = "water"
print(drinks)

#overwrite

drinks ["non-alcoholic"] = "squash"
print(drinks)

#return all values or keys or both

print(drinks.values())
print(print(drinks.keys()))
print(print(drinks.items()))

print("water" in drinks.values())
print("still" in drinks)

#get method

print(drinks.get("still"))
print(drinks.get("stille", "not found"))
print(drinks.get("stillie")) #ask chris to explain

#update

drinks.update({"sugary": "cola"})
#or
drinks.update(very_sugary = "red bull")
print(drinks)

#pop

print(drinks.pop("non-alcoholic"))
print(drinks.pop("non-alcoholic", "not-found"))
print(drinks)

#exercise









#books = { "the cat in the hat": "Dr Seuss", "captain underpants": "Dav Pilky", "diary of a wimpy kid": "Jeff Kinney" }

#books_dict = {"author1": ["book1", "book2"], "author2": ["book3", "book4"]}

#y= input ("enter author name ")
#print(", ".join(books_dict[y])) #ask chris

#tuples
#we can't update in a tuples
#tuples uses () or nothing at all

shapes = ("square", "circles", "triangle")
shapes1 = "square", "circles", "triangle"

print(type(shapes))
print(type(shapes1)) #shows what type of set the above list is

#less memory- very slight 
#speed - a little bit quicker
#indicates that we don't want to change the data

#sets
#no indexing
#no duplicate values
# {}

items = {"apple", "banana", "pear"}

print (type(items)) #shows what type of set the above list is