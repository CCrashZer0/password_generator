import random

amount_of_time = 1
site_name = input("Enter site name: ")
pass_word_length = int(input("Enter password length: "))
upper = int(input("Numher of upppercase letters: "))
lower = int(input("Number of lowercase letters: "))
symbol = int(input("Number of symbols: "))
numbertimes = int(input("Number of numbers: "))


#-------------------------------------------------------------------------------------#
'''
The code above will collect the amount of charcters you want in your password.
Length, symbols, upper, lower.
A strong password will contain all of them. That is why at this point you do not
can not opt out of any the them. 
'''
#-------------------------------------------------------------------------------------#

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * upper
lower = "abcdefghijklmnopqrstuvwxyz" * lower
number = "0123456789" * numbertimes
symbol = "()`~!@#$%^&*-+=|\{}[]:;<>,.?/" * symbol


if (lower == 0):
    alphabet = number + upper
elif (numbertimes == 0):
    alphabet = upper + lower
elif (upper == 0):
    alphabet = number + lower
elif (symbol == 0):
    alphabet = number + symbol
else:
    alphabet = lower + number + upper + symbol

file = open("password.txt","w")
file.write(site_name + ":" + "\n")

for i in range(amount_of_time):
    pw = ""
    for i in range(pass_word_length):
        next_index = random.randrange(len(alphabet))
        pw = pw + alphabet[next_index]
    file.write(pw + "\n")


file.close()
