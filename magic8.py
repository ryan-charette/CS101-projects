import random

name = input("What is your name?")
question = input('Ask a "Yes" or "No" question about the future: ')
random_number = random.randint(0, 8)
answers = ["Yes - definitely.", "It is decidedly so.", "Without a doubt", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful."]



print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answers[random_number])