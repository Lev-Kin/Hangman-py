import random
import sys

words_set = ("python", "java", "swift", "javascript")
win_counter = 0
lose_counter = 0

print("H A N G M A N")
while True:
    user_command = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if user_command == "results":
        print(f"You won: {win_counter} times.\nYou lost: {lose_counter} times.")
    elif user_command == "exit":
        sys.exit()
    elif user_command == "play":
        attempts = 8
        word_goal_saved_print = random.choice(words_set)
        word_goal = list(word_goal_saved_print)
        word_goal_saved = frozenset(word_goal)
        word_hidden = ["-"] * len(word_goal)
        guess_tried = set()

        while attempts > 0:
            print("\n" + "".join(word_hidden))

            guess_letter = input("Input a letter: ")

            if len(guess_letter) != 1:
                print("Please, input a single letter.")
                continue
            elif (guess_letter.lower() != guess_letter) or \
                    (guess_letter.isalpha() is False):
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            elif guess_letter in guess_tried:
                print("You've already guessed this letter.")
                continue
            else:
                guess_tried.add(guess_letter)

            if guess_letter in word_goal:
                for k in range(len(word_hidden)):
                    if guess_letter in word_goal:
                        change_index = word_goal.index(guess_letter)
                        word_hidden[change_index] = guess_letter
                        word_goal[change_index] = "-"
                    else:
                        break
            else:
                attempts -= 1
                if guess_letter in word_goal_saved:
                    print("No improvements.")
                else:
                    print("That letter doesn't appear in the word.")

            if "-" not in word_hidden:
                break

        if attempts > 0:
            print(f"\nYou guessed the word {word_goal_saved_print}!\nYou survived!")
            win_counter += 1
        else:
            print("\nYou lost!")
            lose_counter += 1

