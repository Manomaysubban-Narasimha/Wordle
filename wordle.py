# ----------------------------------------------------------------------
# Name:      Wordle
# Purpose:   implement the wordle game
# Author(s): Manomaysubban Narasimha
# Date:      2022-09-02
# ----------------------------------------------------------------------
"""
A simplified version of the Wordle game.

The program will randomly choose a mystery word, that we'll call wordle,
from some given text (the Sound of Silence song lyrics). The wordle must
have exactly 5 letters with no numbers and no punctuation.
The wordle is in uppercase.
The player has 6 tries to guess the wordle.  For each try, the program
will keep prompting the user for input until they enter a 5-letter word.
Longer or shorter words as well as words that contain non letters
are not accepted.
For each valid guess, the program prints color coded feedback.
Guessed letters are printed in uppercase and in red, yellow or green:
Red indicates that the guessed letter is NOT in the word.
Yellow indicates that the letter is in the word but not in correct spot.
Green indicates that the letter is in the word and in the correct spot.
The game is case-insensitive.  The player may enter the guesses in upper
or lower case. Printed letters in feedback always appear in upper case.
The program also prints a final feedback based on the number of tries:
If the player guesses the wordle in one try, the program prints: Genius!
If player guesses wordle in two tries, the program prints: Magnificent!
If player guesses wordle in three tries,the program prints: Impressive!
If player guesses wordle in four tries, the program prints: Splendid!
If player guesses wordle in five tries, the program prints: Great!
If player guesses wordle in six tries, the program prints: Phew!
If player does not guess answer with six tries, the program prints the
correct answer and exits.
"""

import string
import random
import copy

# Constant assignments
RED = '\033[91m'     # to print text in red: print(RED + text)
GREEN = '\033[92m'   # to print a letter in green: print(GREEN + text)
YELLOW = '\033[93m'  # to print a letter in yellow: print(YELLOW + text)
DEFAULT = '\033[0m'  # to reset the color print(DEFAULT + text)
WORDLE_LEN = 5
MAX_VALID_ATTEMPTS = 6
TOTAL_WORDLES = 35
SOURCE = '''
            Hello darkness, my old friend
            I've come to talk with you again
            Because a vision softly creeping
            Left its seeds while I was sleeping
            And the vision that was planted in my brain
            Still remains
            Within the sound of silence
            In restless dreams, I walked alone,
            Narrow streets of cobblestone
            beneath the halo of a street lamp
            I turned my collar to the cold and damp.
            When my eyes were stabbed by the flash of a neon light
            That split the night
            And touched the sound of silence
            And in the naked light, I saw
            Ten thousand people, maybe more
            People talking without speaking
            People hearing without listening
            People writing songs that voices never shared
            And no one dared
            Disturb the sound of silence
            "Fools" said I, "You don't know
            Silence like a cancer grows.
            Hear my words that I might teach you
            Take my arms that I might reach you"
            But my words, like silent raindrops fell
            And echoed in the wells of silence
            And the people bowed and prayed
            To the neon god they made
            And the sign flashed out its warning
            In the words that it was forming
            Then the sign said, "The words on the prophets are written on the 
            subway walls
            In tenement halls"
            And whispered in the sound of silence
        '''


def choose_wordle(text: str) -> str:
    """
    Chooses a wordle (a 5-letter word without any numbers or
    punctuation) from the input text after having removed all the
    non-alphabets from the text.
    :param text: (string) text from which to choose the mystery word
                 must be passed as a parameter.  Do NOT use the constant
    :return: (string) the mystery word in uppercase
    """
    # enter your code below and take out the pass statement
    # the function should work with any text passed as a parameter.
    # Do NOT use the SOURCE constant directly inside this function.

    for punc in string.punctuation:
        text = text.replace(punc, '')

    # create 2 lists to avoid skipping over certain elements while
    # iterating
    # over the list and removing items at the same time
    text_list = text.split()
    wordle_list = [word for word in text_list if len(word) == WORDLE_LEN]

    for word in text_list:
        for letter in word:
            if not letter.isalpha():
                wordle_list.remove(word)

    # print(f"len of wordle list is {len(wordle_list)}")
    assert len(wordle_list) == TOTAL_WORDLES, "Wrong amount of wordles error"

    wordle = random.choice(wordle_list).upper()

    # while wordle != "BOWED": # for testing purposes
    #     wordle = random.choice(wordle_list).upper()  # testing purpose
    # print(f"The wordle is {wordle}")  # for testing purposes

    return wordle


def check(wordle: str, guess: str) -> str:
    """
    Checks whether the guess is equal to the wordle by comparing the
    wordle against the guess character-by-character, and returns a
    color-coded version of the guessed word to indicate the result of
    the comparison. The colors are assigned as follows:
    If the letter in the guess is at the same position in the wordle as
    well, then the color of the letter in guess would be green.
    If the letter in guess is in the wordle, but at a different position
    then the color of the letter in guess would be yellow.
    If the letter in guess is not present in wordle at all, then the
    letter would be colored red.
    :param wordle: (string) the mystery word
    :param guess: (string) the user's guess
    :return: (string) a string of red, yellow or green uppercase letters
    """
    # enter your code below and take out the pass statement
    # HINTS: create a working list of letters in the wordle
    # go over the letters in the guess and check for green matches
    # add the green matches to their correct position in an output list
    # remove the green matches from the working list
    # go over the letters in the guess again
    # compare them to the letters in working list
    # add yellow or red color and add them to their position in output
    # list
    # join the output list into a colored string

    wordle_lets = list(wordle)
    guess_lets = [letter.upper() for letter in guess]
    output_list = ["" for _ in range(WORDLE_LEN)]

    pop_indices = list()

    for i, (wordle_let, guess_let) in enumerate(zip(wordle_lets,
                                                    guess_lets)):
        if wordle_let == guess_let:
            output_list[i] = GREEN + wordle_let + DEFAULT
            pop_indices.append(i)

    i = 0
    for index in pop_indices:
        index = index - i
        wordle_lets.pop(index)
        guess_lets.pop(index)
        i += 1

    match_dict = {}

    for let in wordle_lets:
        if let in match_dict:
            match_dict[let] += 1
        else:
            match_dict[let] = 1

    for i, let in enumerate(guess_lets):
        if let in match_dict:
            guess_lets[i] = YELLOW + let + DEFAULT
            match_dict[let] -= 1
            if not match_dict[let]:
                del match_dict[let]
        else:
            guess_lets[i] = RED + let + DEFAULT

    for i, let in enumerate(output_list):
        if not let:
            output_list[i] = guess_lets.pop(0) + DEFAULT

    output_str = ''.join(output_list)
    return output_str


def all_attempts(wordle: str) -> bool:
    """
    Allows the user up to six attempts to guess the wordle.
    If the user guesses within 1 attempt, then prints "Genius!"
    If the user uses 2 attempts, then prints "Magnificent!"
    If the user uses 3 attempts, then prints "Impressive!"
    If the user uses 4 attempts, then prints "Splendid!"
    If the user uses 5 attempts, then prints "Great!"
    If the user uses 6 attempts, then prints "Phew!"
    If the user cannot guess within 6 attempts, then prints the
    correct answer.
    :param wordle: (string) word to be guessed in upper case
    :return: (boolean) True if player guesses within 6 attempts and
             False otherwise
    """
    # enter your code below and take out the pass statement
    # use the check function to build the colored feedback string
    num_of_attempts = 1

    while num_of_attempts <= MAX_VALID_ATTEMPTS:
        print(f"Attempt {num_of_attempts}")
        valid = False
        guessed_word = None
        while not valid:
            guessed_word = input("Please enter your 5-letter guess: ")\
                            .upper()
            if len(guessed_word) == WORDLE_LEN:
                for letter in guessed_word:
                    if not letter.isalpha():
                        break
                else:
                    valid = True

        print(check(wordle, guessed_word))
        default_list = [DEFAULT + 'A']  # bring back text color to black

        if wordle == guessed_word:
            match num_of_attempts:
                case 1:
                    print("Genius!")
                    return True
                case 2:
                    print("Magnificent!")
                    return True
                case 3:
                    print("Impressive!")
                    return True
                case 4:
                    print("Splendid!")
                    return True
                case 5:
                    print("Great!")
                    return True
                case 6:
                    print("Phew!")
                    return True
        else:
            num_of_attempts += 1
    else:
        return False


def main():
    # enter your code following the outline below and take out the
    # pass statement.
    # 1.call choose_wordle to get the mystery word in uppercase
    # 2.call all_attempts to give the user 6 tries
    # 3.if the user has not guessed the wordle, print the correct answer
    wordle = choose_wordle(SOURCE)
    completed_within_six = all_attempts(wordle)
    if not completed_within_six:
        print(f"The correct answer is {wordle}")


if __name__ == '__main__':
    main()

