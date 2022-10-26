import random


def loadWords():
    word_list = ['python', 'java', 'swift', 'javascript']
    return random.choice(word_list)


word = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    if c == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    s = []
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '-'
    return ans


def getAvailableLetters(lettersGuessed):
    import string
    ans = list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)


def hangman(secretWord):
    print("H A N G M A N")
    print()
    hidden = len(word)
    hint = "-" * hidden
    print(hint)

    global lettersGuessed
    turns = 0
    lettersGuessed = []

    while 8 - turns > 0:
        turns += 1
        if isWordGuessed(secretWord, lettersGuessed):
            continue

        else:

            guess = str(input("Input a letter: ")).lower()
            print()

            if guess in secretWord and guess not in lettersGuessed:

                lettersGuessed.append(guess)
                print(getGuessedWord(secretWord, lettersGuessed))

            else:
                if (guess in secretWord and guess in lettersGuessed):
                    print(getGuessedWord(secretWord, lettersGuessed))
                    continue

                lettersGuessed.append(guess)
                print("That letter doesn't appear in the word.")
                print()
                if 8 - turns > 0:
                    print(getGuessedWord(secretWord, lettersGuessed))

        if 8 - turns == 0:
            print("Thanks for playing!")
            break

        else:
            continue


secretWord = word.lower()
hangman(secretWord)
