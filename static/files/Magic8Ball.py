# ------------------------------------------------------
#        Name: Lauren Forando
#    Filename: Magic 8 Ball
#        Date: 3/01/19
# ------------------------------------------------------

#Establish interesting introduction
def intro():
    opening_question = input(("Wanna Play a Game?... (YES/NO) : ")).upper()
    if (opening_question == "YES"):
        print("Let's Begin! o.o")
    else:
        print("Too Bad ¯\_(ツ)_/¯")

#Creating an interesting graphic
def header():
    top_dash = ("_____")
    bottom_dash = ("-"*len(top_dash))

    print(" "*(len(top_dash)//2))
    print("{0:>7}".format(top_dash))
    print(" /", " "*(len(top_dash)-2), "\\")
    print("|", " "*(len(top_dash)//3), "8", " "*(len(top_dash)//3), "|")
    print(" \\", " "*(len(top_dash)-2), "/")
    print("{0:>7}".format(bottom_dash))
    print(" ")
    print(" ")

#Imported random from Python
import random

#Put the 20 possible responses in a list so that the random function could treat each item based on its index
responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
              "You may rely on it.", "As I see it yes.", "Most likely.", "Outlook good.", "Yes.",
              "Signs point to yes.", "Reply hazy try again", "Ask again later.", "Better not tell you now.",
              "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
              "My sources say no.", "Outlook not so good.", "Very doubtful."
              ]

#Defined the function using main()
def main():
    intro()
    header()
    
    #Then, established the first input: "start_question"
    start_question = input("Enter your question for the Magic 8 Ball: ")
    
    #Placed a print function to generate a random response cached in the list once prompted with the "start_question"
    print("The Magic 8 Ball says...", random.choice(responses))
    
    #Then, established the second input: "repeat_question". Added .upper() to the end of the input so that the function wouldn't be case sensitive.
    repeat_question = input("Would you like to ask another question? YES/NO: ").upper()
    
    #Next, created a while loop to respond to the answer of the "repeat_question" so the loop runs continuously over the condition: (repeat_question != "N") 
    while (repeat_question != "NO"):
        start_question = input("Enter your question for the Magic 8 Ball: ")
        print("The Magic 8 Ball says...", random.choice(responses))
        repeat_question = input("Would you like to ask another question? YES/NO: ").upper()
        
    #The print statement is the function's "stop" condition once the user inputs "NO" or "no" when prompted with "repeat_question"
    print("That's a wrap!")
    

if __name__ == "__main__":
    main()


