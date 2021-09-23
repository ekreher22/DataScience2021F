import random 

# choosing random word
word_options = ['apple', 'banana', 'cherry']
word = random.choice(word_options) 
print(word)

def play_hangman():
    print ('Welcome to Hangman!')
    print ('The secret word has ' + str(len(word)) + ' letters and the theme is fruit') 
    word_letters = set(word) # list of letters in the word
    used_letters = set()
    num_of_guesses = 0
    max_num_of_guesses = 10
    gameover = False
    while (num_of_guesses < max_num_of_guesses) & (gameover == False):
        user_guess = input ('Enter guess:').lower()
        if user_guess in word_letters:
            print('Yes, "' + str(user_guess) + '" is in the word!')
            word_letters.remove(user_guess)
            used_letters.add(user_guess)
            num_of_guesses += 1
        elif user_guess in used_letters:
            print('You already guessed that letter')
        else:
            print('Not one of the letters!')
            used_letters.add(user_guess)
            num_of_guesses += 1
         
        print('So far you have: ')
        # so far you have guessed here
        print('You have guessed:\n' +  str(used_letters))
        #num_of_guesses += 1
        print('You have ' + str((max_num_of_guesses - num_of_guesses)) +' guesses left.')
        #print(word_letters)
        if word_letters == set():
            print('You guessed the word!')
            gameover = True
        
    print('the game is over')
  
play_hangman()


# create 'so far you have ****e* '



    