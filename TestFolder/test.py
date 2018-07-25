print("hello world")
answer = input("Who inspires you? ")
print(answer, "inpires you!")
i = 0
while i < 5:
    print(i)
    i += 1
for i in range(5):
    print(i)
i = -1 #assinged i=-1
while True: #while the folling is true
   i += 1 #increment i by 1

   if(i > 20): #If i > 20 then
        break #stop the loop


   if(i % 2 !=0): #if i is odd
            continue

   print(i)



from random import *
arandomnumber = randint(1,100)
guess= input("Guess a number between 1 and 100 (inclusive): ")
if not guess.isnumeric():
    print("Thats not a positive whole number, try again!")
else:
    guess = int(guess)

for x in range(10):
    if guess > arandomnumber:
       print("Wrong, try again! This time guess lower.")
       guess= int(input("Guess a number between 1 and 100 (inclusive): "))
       continue
    elif guess < arandomnumber:
        print("Wrong, try again! This time guess higher.")
        guess= int(input("Guess a number between 1 and 100 (inclusive): "))
        continue
    elif guess == arandomnumber:
       print("CORRECT! You guessed the number! Have a free puppy")
       break
name = input("What is your name?: ")

print ("Hello",name,". Welcome to your story. One morning you were playing soccer in your yard. Your family had just bought the castle where you live.")
print ("A bat appears..")
print ("The bat says, MUAHAHAHA, this is my castle and you must go or I will end you!")
user_input= input("Type 'run' to run away from bat or 'talk' to talk to bat: ")
if (user_input == "run"):
    print ("You run away from the bat and enter the castle.")
elif (user_input == "talk"):
   print ("You decide to talk it out with the bat about living together in the castle peacefully.")
   print ("The bat says to go away before I kill you!")
   print ("You turn and run to the castle...")



print ("You run into the kitchen and see a clove of garlic ")
user_input2= input("Type 'take garlic' or 'leave garlic': ")
if (user_input2 == "take garlic"):
   print ("You grab the garlic and throw it at the bat...")
   print ("The bat screeches and you run into your bedroom")
elif (user_input2 == "leave garlic"):
   print ("You leave the garlic and run into your room")

print ("You're in your bedroom and feel tired. You go to bed and wake up the next morning")

user_input3= input("Type 'dream' if you think there was never a bat and type 'bat' if you think it wasn't a dream: ")
if (user_input3 == "dream"):
   print("You say hallelujah and order a pizza. The end")
elif (user_input3 == "bat"):
   print ("The bat comes into your room, eats your head off, and you die. The end. ")


friends = ["Beyonce", "Jay-Z", "XXXTENTACION", "Kodak Black", "Post Malone"]
# weights = [153.4, 81.2, 1293.4, 432.6]
random_data = ["George", 8, 10.2]


cmd + / = multiline comment [#]

print(friends)
print(len(friends))
print("Amanda" in friends)

for num in friends:
    print(num)

for name in range(len(friends)):
    print (friends[name])

anExample= "ada!"
print(len(friends)) #number of elements in my list:
#output: 4
print(len(anExample)) #number of characters in my string
print("da" in anExample)
#output: true
print(anExample[2])
print(anExample[2] + anExample[1])
for letter in anExample:
    print(letter)

anExample= "Dorothy"
print(anExample)
print("Each character in my string:")
for character in anExample:
        print(character)  #prints each letter[character] vertically

print(friends)
print("each element in my string:")
for element in friends:
    print(element)


#LIST PRACTICE:
print("Hello, today we will go over information about lists")
print("How is the length of a list and the index of the last item related?")
list1 = ["Apple", "Bananna", "Pear", "Grapes"]
print("Index of the last item: ")
print(list1[3]) #Index of the last item
print("Length of the list: ")
print(len(list1)) #length of list
print("This shows that ")
#the index of the last item is the length of the list -1, bc computers start counting at 0
#What else do you think you can put in lists?
print("What else do you think you can put in lists?")
list2 = ["1", "2", "3", "4",]
list3 = [radint(1,10),radint(10,20),radint(20,30),radint(30,40)]

Do you think all items must be the same data type?


Can you put a list in the list?


list.append(element)
list.insert(index,element)
list.remove(element)
list.sort()
list.reverse()

functions:
  remove(element) -removes element from the list
  append(element) -adds al element to the end of the list
  insert(index, element) -inserts an element in a specific Index
  sort()  -sorts the list in acsending order
  reverse() - reverse the list

list= [7,7,16,81,40,"foo"]
list.remove(list[3])
list.remove(7) #removes () from list
list.append(500) #adds to end
list.insert(3,"lunchtime!")
list.remove("foo")
list.sort()
print(list)


NAME GENERATOR
from random import *
listnames = ["Micheal","Jim", "Pam", "Creed", "Ryan"]
aRandomIndex = randint(0, len(listnames)-1)
print("You are: ")
print(listnames[aRandomIndex])

MENU
from random import *
Drink = ["Rain Water","White Wine", "Straight Tequila"]
Appetizer = ["Bread and Butter", "Cow Tongue", "Bruschetta"]
Main_Course = ["Escargot", "Pizza", "nothing, u starve"]
Dessert = ["Ice Cream", "freeze dried toads", "frozen cat eyeballs"]
aRandomIndex = randint(0, len(Appetizer)-1)
aRandomIndex2 = randint(0, len(Drink)-1)
aRandomIndex3 = randint(0, len(Main_Course)-1)
aRandomIndex4 = randint(0, len(Dessert)-1)
print("Menu for Tonight:")
print(Appetizer[aRandomIndex])
print(Drink[aRandomIndex2])
print(Main_Course[aRandomIndex3])
print(Dessert[aRandomIndex4])

HAIKU
from random import *
sevensyllables= ["Standing in front of a door", "describing the world we see", "the best of humanity"]
fivesyllables= ["I eat carrots. Why?", "Always live prepared", "Stride by Stride, I fly"]
fivesyllables2= ["Sendem to the end", "You are summers start", "dont apologize"]
aRandomIndex= randint(0, len(fivesyllables)-1)
aRandomIndex2= randint(0, len(sevensyllables)-1)
aRandomIndex3= randint(0, len(fivesyllables2)-1)
print(fivesyllables[aRandomIndex])
print(sevensyllables[aRandomIndex2])
print(fivesyllables2[aRandomIndex3])

Hangman:
print("-----------------------------------------------")
print("WELCOME TO THE HANGMAN GAME!")
dashes= []
while True:
    word = input("Type a word for someone to guess: ")
    if word.isalpha() == False:
        print("Thats not a word! Try Again")
    else:
        numberofletters= (len(word))
        for everyletter in range(numberofletters):
            dashes.append("_")
        print("-----------------------------------------------")
        print(dashes)
        print("-----------------------------------------------")
        break
while True:
    guess= input("Guess a letter: ")
    if guess.isalpha() == False:
        print("Thats not a letter! Try again.")
    elif len(guess) !=1 :
        print("Your guess must only have one letter! Try again.")
    if guess in str(word):
        indexofword = word.index(guess)
        print("Congrats that letter is in the word!")
        dashes.pop(indexofword)
        dashes.insert(indexofword,guess)
        print(dashes)







        for guess in range(len(wor
        d)):
            #dashes.remove(indexofword)
            dashes.insert(indexofword, guess)
            print(dashes)
                dashes.remove("_")
                print(dashes)



indexofword = word.index(guess)
guesses_left= 10
while guesses_left > -1 and not dashes == word:
    print(guesses_left)
    break
#
if guess



    print("That letter is in the word!")
    dashes= update_dashes(word, dashes, guess)
elif :
    print("That letter is not in the word!")
    guesses_left= -1
guesses_left = 10
while guesses_left > -1 and not dashes == word:
    print(guesses_left)
    break
    if dashes == word:

print(str(guesses_left))
guess= input("Guess a letter: ")

elif guess in word:
    print("That letter is in the word!")
    dashes= update_dahes(word, dashes, guess)
else:
    print("That letter is not in the secret word!")
    guesses_left = -1
if guesses_left <0:
    print ("You lose. The word was: " + str(word))
else:
    print ("Congrats!! You win. The word was: " + str(word))
def update_dashes(secret, cur_dash, rec_guess):
    result = ""
    for i in range(len(secret)):
        if secret[i] == rec_guess
            result = result + rec_guess
        else:
            result = result + cur_dash[i]
    return result




def repeat_to_length(string_to_expand, lenght):

guesses= [10]
maxfails= 7

while word = False
#converst word to lowercase
word = word.lower()

#some useful variables
maxfails = 7
guess = input("Guess a letter: ")


#if a number is even, we skip it
if(number % 2 === 0):
    continue





FINDING AVERAGE
numbers= [5,12,3,56,24,78,1,15,44] #create list
average = 0
sum = 0
for elements in numbers:
    sum= sum + elements
average= sum / len(numbers)
print(average)
numbers.sort() # sort list
sum(numbers)
len(numbers)
average= (sum(list)) / len(list)
print(average)
sumofages
rangeOfAges= ages[len(ages)-1] - ages[0] #subtract the frist item from the last item
print(rangeOfAges) #print the value
