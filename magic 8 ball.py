import sys
import random
import time

start = input("So you want to play magic 8 ball? Yes or no? ")

if start == "yes":
    print("okay, lets play!")  # setting up
    time.sleep(1)
    name = input("What is your name? ")

    print("entering name into system....")  # makes it look loading
    time.sleep(1)
    print("entering name into system....")
    time.sleep(.5)

else:
    if start == "no":
        sys.exit("okay goodbye!")  # not want to play 8ball
    time.sleep(.5)
loop_option = ''
while loop_option!= "no":                #loop begins
    question = input("Ask a question. ")

    values = ["ayyyy your in luckk %s " % name, "nah %s " % name, "no way %s " % name]  # answers

    answer = print(random.choice(values))  # random answer generator

    loop_option: str = input("do you want to play again? yes or no? ")     #user exit if want
