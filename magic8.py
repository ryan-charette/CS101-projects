#Write a Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
#The output of the program will have the following format:
    #[Name] asks: [Question]
    #Magic 8-Ball’s answer: [Answer]

import random
import sys

name = input("What is your name? ")
question = input('Ask a "Yes" or "No" question about the future: ')
random_number = random.randint(0, 19)
answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

if question == "":
    print("It is forbidden to provide a fortune to those who do not ask a question.")
    sys.exit()
elif name == "":
    print("Question: " + question)
else:
    print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answers[random_number])
