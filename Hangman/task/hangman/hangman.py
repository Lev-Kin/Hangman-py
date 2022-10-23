import random

print('H A N G M A N')

words = ['python', 'java', 'swift', 'javascript']
x = random.choice(words)

print('Guess the word: ')
word = input()
if word == x:
    print('You survived!')
else:
    print('You lost!')
