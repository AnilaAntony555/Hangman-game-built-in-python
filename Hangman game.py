import random

def play_hangman():
    Name = input("What is your name? ")
    print('Hi', Name, 'Are you ready to play the Hangman game?')
    Ans = input('YES or NO: ').upper()

    if Ans == "YES":
        print('What is Hangman game?')
        print('The Hangman randomly selects a secret word from a list of secret words.\n'
              'When a letter in that word is guessed correctly, that letter position in the word is made \n'
              'visible. In this way, all letters of the word are to be guessed before \n'
              'all the chances are over. For convenience, we have given the length of the word + 2 chances. For example, \n'
              'if the word to be guessed is "mango", then the user gets 5 + 2 = 7 chances, as "mango" is a five-letter word.')

        print('Guess the word! Hint: The word is the name of a bird.')


        Birds_name = ['duck', 'ostrich', 'flamingo', 'toucan', 'pigeon', 'peacock']

        word = random.choice(Birds_name).lower()
        no_of_attempt = len(word) + 2
        print('Maximum number of attempts is', no_of_attempt)
        print("All the best", Name)

        guessed_word = ['-' for _ in word]
        guessed_letters = []

        turn = 0
        while turn < no_of_attempt:
            print("Current word: ", ' '.join(guessed_word))


            if turn > 0:
                F1 = input("Enter a letter or guess the full word: ").lower()
            else:
                F1 = input("Enter a letter: ").lower()


            if len(F1) > 1:
                if F1 == word:
                    print("Congratulations! You guessed the word",word,"correctly and won the game.")
                    break
                else:
                    print("Oops! That's not the correct word.")
                    turn += 1
                    continue


            if len(F1) != 1 or not F1.isalpha():
                print("Please enter a single valid letter.")
                continue


            if F1 in guessed_letters:
                print("You already guessed that letter. Try a different one.")
                continue

            guessed_letters.append(F1)

            if F1 in word:
                for i in range(len(word)):
                    if word[i] == F1:
                        guessed_word[i] = F1
                print("Good guess!")
            else:
                print("Oops! That letter is not in the word.")

            turn += 1

            if ''.join(guessed_word) == word:
                print('Congratulations! You won the game.')
                break
        else:
            print('You lose, better luck next time.')
            print(f"The word was: {word}")

    else:
        print('Play later!')
        return


    play_again = input("Do you want to play again? (YES or NO): ").upper()
    if play_again == "YES":
        play_hangman()
    else:
        print("Thank you for playing! Goodbye!")


play_hangman()

