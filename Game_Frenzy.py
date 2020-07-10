import random
from random import randint
from FamousThings import Tallest_Buildings

t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0, 2)]

def get_word():
    word = random.choice(Tallest_Buildings)
    return word.upper()

def play(word):
    player = False
    answer = ["win", "lose", "tie"]

    while player == False:
        player = input("Rock, Paper, Scissors? \n")
        print("\n")

        if player == computer:
            answer = 'tie'
            print("Tie!")

        elif player == "Rock":
            if computer == "Paper":
                answer = 'lose'
                print("You lose!", computer, "covers", player)
            else:
                answer = 'win'
                print("You win!", player, "smashes", computer)

        elif player == "Paper":
            if computer == "Scissors":
                answer = 'lose'
                print("You lose!", computer, "cut", player)
            else:
                answer = 'win'
                print("You win!", player, "covers", computer)

        elif player == "Scissors":
            if computer == "Rock":
                answer = 'lose'
                print("You lose...", computer, "smashes", player)
            else:
                answer = 'win'
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling! \n NB: Words are Case Sensitive")

        if answer == 'win':
            word_completion = "_" * len(word)
            guessed = False
            guessed_letters = []
            guessed_words = []
            tries = 3
            print("Ready??????????? \n LETS PLAY :-} \n HINT: TALLEST BUILDINGS IN THE WORLD!")
            print(word_completion)
            print("\n")
            while not guessed and tries > 0:
                guess = input("Please guess a letter or word: ").upper()
                if len(guess) == 1 and guess.isalpha():
                    if guess in guessed_letters:
                        print("You already guessed the letter", guess)
                    elif guess not in word:
                        print(guess, "is not in the word.")
                        tries -= 1
                        guessed_letters.append(guess)
                    else:
                        print("Good job,", guess, "is in the word!")
                        guessed_letters.append(guess)
                        word_as_list = list(word_completion)
                        indices = [i for i, letter in enumerate(word) if letter == guess]
                        for index in indices:
                            word_as_list[index] = guess
                        word_completion = "".join(word_as_list)
                        if "_" not in word_completion:
                            guessed = True
                elif len(guess) == len(word) and guess.isalpha():
                    if guess in guessed_words:
                        print("You already guessed the word", guess)
                    elif guess != word:
                        print(guess, "is not the word.")
                        tries -= 1
                        guessed_words.append(guess)
                    else:
                        guessed = True
                        word_completion = word
                else:
                    print("Not a valid guess.")
                print(word_completion)
                print("\n")
            if guessed:
                print("Congrats, you guessed the word! You win!")
            else:
                print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

        elif answer == 'tie':
            print("Y'all should play again")

        elif answer == 'lose':
            print("Computer Wins and has a Play :-}")
        else:
            print("Play Again :-(")
def main():
    word = get_word()
    play(word)

    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
if __name__ == "__main__":
    main()

player = False
computer = t[randint(0,2)]


