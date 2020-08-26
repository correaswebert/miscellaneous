
#############################################

from random import randint

words = open('/home/mr-anon/Projects/words.txt', 'r')

word_list = words.readlines()
x = randint(0, len(word_list)-1)
word = word_list[x].strip('\n')
word_len = len(word) - 1

words.close()

#############################################

letters = ''
for x in word:                                     # to avoid letter repetition
    if x not in letters:                           # eg. 'sissy' -> 'siy'
        letters += x
    

lives = 7
hints_used = 0
correct_guess = 0
wrong_guess = 0

print("\nYou have %d lives" % lives)

lettersGuessed = ''

#############################################

def autofill(length):

    ans1, ans2, ans3 = '', '', ''
    x, y, z = 0, 0, 0
    
    word = str(length)
    if word_len <= 4:
        x += randint(0, word_len)
        ans1 = word[x]

    elif word_len <= 8:
        x += randint(0, (word_len)//2)
        y += randint(4, word_len)
        ans1, ans2 = word[x], word[y]
        
    else:
        x += randint(0, (word_len)//3)
        y += randint(4, 2*(word_len)//3)
        z += randint(8, word_len)
        ans1, ans2, ans3 = word[x], word[y], word[z]

    return ans1, ans2, ans3

#############################################

autofill = autofill(word)
lettersGuessed += autofill[0]
lettersGuessed += autofill[1]
lettersGuessed += autofill[2]

#############################################

def answer_letter():

    x = list(word)
    y = list(lettersGuessed)
    z = [c for c in x if c not in y]
    rand = randint(0,len(z)-1)

    return z[rand]

#############################################

print("You are always free to spend two lives to reveal a letter!\
        Just type 'hint'.\n")

while lives > 0:

    for char in word:
        if char in lettersGuessed:
            print(char, end=' ')
        else:
            print("_ ", end=' ')       # not "_ " as end="\n" by default

    guess = input("\nEnter a letter to guess: ").lower()
    
    if guess == 'hint':
        guess = answer_letter()
        lives -= 2
        hints_used += 1
        print("\nLives remaining are %d" % lives)

    if guess in word:
        if guess in lettersGuessed:
            print('\nYou already guessed that!\n\n')
        else:
            lettersGuessed += guess
            correct_guess += 1
            print('\n')
    
    else:
        lives -= 1
        wrong_guess += 1
        print("\nLives remaining are %d\n\n" % lives)

        if lives == 0 :
            print("You lose!")

    if len(letters) == len(lettersGuessed) :
        print(word)
        print("You won!")        
        break

# #############################################

# def score(correct_guess, wrong_guess, hints_used, lives):
#     score = 0
#     score += (correct_guess * 100) - (wrong_guess * 30) - \
#              (25 * hints_used) + (50 * lives)
#     return score

# score = score(correct_guess, wrong_guess, hints_used, lives)

# #############################################

# from datetime import datetime
# time = str(datetime.now().hour) + ":" + str(datetime.now().minute)
# date = str(datetime.now().day) + "." + str(datetime.now().month) + \
#           "." + str(datetime.now().year)
# current = date + ' ' + time

# #############################################

# import login
# ask = input("\nWould you like to save your progress? (y/n)\n>").lower()
# if ask == 'y':
#     ask = input("Do you have an existing account? (y/n)\n>").lower()
#     if ask == 'y':
#         login.login(score, current)
#         print("Progress saved.")
#     else:
#         login.logon(score, current)
#         print("Progress saved.")
        

# #############################################

# import pygame,sys

# GREY = (128,128,128)
# p1 = (60,100)

# pygame.init()
# SCREEN = pygame.display.set_mode((300,300))
# pygame.display.set_caption("Hangman Game")
# #head and body
# pygame.draw.circle(SCREEN, GREY, (150,50), 30, 5)
# pygame.draw.line(SCREEN, GREY, (150,80),(150,180),6)
# #legs
# pygame.draw.line(SCREEN, GREY, (150,180),(110,220),6)
# pygame.draw.line(SCREEN, GREY, (150,180),(190,220),6)
# #hands
# pygame.draw.line(SCREEN, GREY, (150,120),(110,110),6)
# pygame.draw.line(SCREEN, GREY, (150,120),(190,110),6)

# pygame.display.update()
