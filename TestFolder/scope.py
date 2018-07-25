# # CHATBOT:
# # --- Define your functions below! ---
# # answer
#
# def intro():
#     print()
#     print("Hi, Welcome to chatbot!")
#     print("Please talk to me!")
#     print()
#
# def process_input(answer, name):
#     if answer == "hello":
#         say_greeting(answer, name)
#     else:
#         say_bye()
#
# def say_greeting(answer, name):
#     print()
#     print("Oh Hi!")
#     print("Nice to you meet you, %s!" % name)
#     print()
#
# def say_bye():
#     print()
#     print("See ya.")
#     print()
#
#
# # --- Put your main program below! ---
# def main():
#     intro()
#     while True:
#         user = input("whats your name?: ")
#         answer = input("What will you say? ")
#         process_input(answer, user)
#
# # DON'T TOUCH! Setup code that runs your main() function.
# if __name__ == "__main__":
#     main()
#
#
# def say_hello(name):
#     print("Hi " + name)
#
# def main():
#     user = "Michelle"
#     say_hello(user)
#
# if __name__ == "__main__":
#     main()
#

#CHAT BOT
def welcome():
    print()
    answer_name= input("What's your name?: ")
    print()
    print("Hello %s!" %answer_name)
    print()
    print("Hello, I am your computer, lets have a conversation!")
    print()


def proccess_input():
    print()
    answer_talk= input("What would you like to talk about? I can talk about Weather, Sports, or Food: ")
    print()
    if answer_talk == "Weather" :
        weather()
    if answer_talk == "Sports" :
        sports()
    if answer_talk == "Food" :
        food()

def weather():
    print()
    print("Weather! Great, thats my favorite topic!")
    print()
    input("Hows the Weather looking outside for you right now?: ")
    print()
    print("Wonderful!! I love all kinds of weather, the idea of weather just sounds so magical.")
    print()
    print("As you could expect, since I am a computer, I have never really experienced weather myself.")
    print()
    moveon= input("What would you like to discuss next? Sports? Food?: ")
    print()
    if moveon == "Sports":
        sports()
    if moveon == "Food":
        food()

def sports():
    print()
    print("Sports! Great thats my favorite topic!")
    print()
    sports= input("Which sport do you prefer? Baseball or Basketball?: ")
    print()
    if sports == "Baseball":
        print()
        print("Baseball! Yay! GO GIANTS!")
        print()
        print("Ya the giants are definitely my favorite baseball team, mostly because I was made in SF but also becuase they are actually good. haha.")
        print()
    if sports == "Basketball":
        print()
        print("Basketball! Yay! GO WARRIORS!")
        print()
        print("Ya the warriors are definetely my favorite basketball team, mostly because I was made in SF but also because they are the best, and always win. hahaha.")
        print()
    moveon2= input("What would you like to discuss next? Food? Weather?: ")
    print()
    if moveon2 == "Weather":
        weather()
    if moveon2 == "Food":
        food()

def food():
    print()
    print("Food! WOHO, I like food.")
    print()
    input("Whats your favorite Food?: ")
    print()
    print("Delicious! Yeah, I have never tasted food, being a computer and all.")
    print()
    print("I have read quite a few descriptions on what food tastes like and sometimes, I can almost smell a delicious pizza in my harddrive.")
    print()

def bye():
    print()
    print("Well, I have a lot of very important buissness to attend to, Bye")
    print()
    print("Talk to you later!!")
# def food():
#     print("Food! Great, thats my favorite topic!" frn)
#     frn= input("Which Food do you prefer? Salads or Pizza?: ")
#
def main():
    welcome()
    proccess_input()
    bye()
if __name__ == "__main__":
    main()
#

# print("Hello! I am your computer, lets have a conversation!")
# name= input("Whats your name?: ")
# print("Hello, %s!" %name)
# conversation= input("What would you like to talk about? Food? Sports? Weather?: ")
# print(conversation)
# answer1= food
#
# answer2= sports
# answer3= weather



#
# def sub(num1, num2):
#     diff = num1 - num2
#     print(diff)
#     return(diff)
#
# def main():
#     n = 10
#     n2 = 2
#     print(sub(n, n2))
#
# if __name__ == "__main__":
#     main()
#
#
#

#
#     user = "Cindy"
#     user2= "Tiffanie"
#     say_hello(user2)
#     say_hello(user)
#
#
#
# def calc_total():
#     numbers= [ 1, 2, 3, 4, 5]
#     sum = 0
#     for elements in numbers:
#         sum = sum + elements
#     print (sum)
#
#
# if __name__ == "__main__":
#     calc_total()

#
# def intro():
#     print()
#     print("Hi, welcome to chatbot!")
#     print("Please talk to me!")
#     print()
#
# def is_valid_input(answer, listOfResponses):
#     #for every item in the list see if answer is equal
#         #if answer is in listOfResponses
#             #return true
#         #else
#             #return True
#     for x in listOfResponses:
#         if answer in listOfResponses:
#             return True
#         else:
#             return False
#
# def process_input(answer, name):
#     greetings= ["Hi", "Hey", "What's up", "Hello"]
#     goodByes= ["bye", "bye bye", "See Ya"]
#
#     if is_valid_input(answer, greetings):
#         say_greeting(answer, name)
#     elif is_valid_input(answer, goodByes):
#         say_bye()
#
# def answer1(answer, name):
#     #if answer == something in the list(greetings)
#         # then say hello, how are you doing
# #    #elif answer == something not in the list
#         #then say sorry, i did not understand that, please start our conversation with a greeting
#
#
# def say_greeting(answer, name):
#     print()
#     print("Oh, HI!")
#     print("Nice to meet you, %s!" % name)
#     print()
#
# def main():
#     intro()
#     while True:
#       name = input("whats your name?: ")
#       answer = input("What will you say? ")
#       process_input(answer, name)
#
#
# if __name__ == "__main__":
#     main()
