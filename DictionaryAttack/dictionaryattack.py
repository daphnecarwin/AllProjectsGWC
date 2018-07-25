#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:
#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
file = open("dictionary.txt","r")

for word in f:
    if word.strip() == test_password.strip():
        print("NO THATS IN THE DICTIONARY")
    else:
        print("YE DAWG,")
        break


#print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
##NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
#test_password = input("Type in a trial password: ")

#if __name__ == '__main__':
    #main()



#if 'test_password' not in f:
    #print("yo")
#elif test_password in "dictionary.txt":
    #print("yup")






#Write logic to see if the password
