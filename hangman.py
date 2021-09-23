import random 

# choosing random word
word_options = ['apple', 'banana', 'cherry']
word = random.choice(word_options) 
print(word)
#print(len(word))


def play_hangman():
    print ('Welcome to Hangman!')
    word_letters = set(word)
    #print ('The secret word has ' + len(word) + ' letters and the theme is fruit') 
    print(word_letters)
    used_letters = set()
    user_guess = input ('Enter guess:').lower()
    used_letters.add(user_guess)
    print(user_guess) 
    if user_guess in word_letters:
        print('You guessed a letter!')
        word_letters.remove(user_guess)
    elif user_guess in used_letters:
        print('You already guessed that letter')
    else:
        print('Not one of the letters!')
        
    
play_hangman()



#print (num)
#print (' letters and the theme is fruit!')


#guesses = []
#finish = False

#while finish == False:
    
#guessed_letters = [(input("Enter guess: "))]




#list_size = int(input("Enter the number of sub list "))

#print("\n")

#print(guessed_letters)


#while True:
   # guessed_letters = [(input("Enter guess: "))]
   # if guessed_letters == 'stop': break
   # print(guessed_letters)
   # figure out how to stop 
    