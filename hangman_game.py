## Hangman Game

import random
picture = ["""
   +---+
   |   |
       |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""]

word = []
used = set()


with open("word.txt","r") as file:
    for line in file:
        word.append(line)

choose = random.choice(word)
choose = choose.upper()
k=0
size = len(choose) - 1
outline = list('_' * size)
print(picture[k])
print(' '.join(outline), end=' ')

lives = 6
while(lives > 0): 
    
    print("You have ",lives,"lives left and the words you used: "," ".join(used))
    user_word = input("Enter the Guessing word: ").upper()
    if user_word in used:
        print("Do not enter the same words, please")
        continue
    
    elif len(user_word) > 1:
        print("Enter just a word, please.")
        continue
    
    elif user_word not in choose:  
        lives -= 1
        k = k + 1
        print(picture[k])
        used.add(user_word)
        
    else:
        for j in range(len(choose)):
            if user_word == choose[j]:
                outline[j] = user_word
                used.add(user_word)
        print(' '.join(outline), end=' ')
        
    if lives == 0:
        print("TRY AGAIN\nWORD is {}".format(choose))
        break
    
    if "_" not in outline:
        print("\nCONGRULATIONS")
        break

input("Press exit")





