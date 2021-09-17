words = ['apple', 'banana', 'cherry']
num = len(words[1])
#print (num)

print ('Welcome to Hangman!')
#print ('The secret word has ' + num + ' letters and the theme is fruit!')

#input ('Enter guess:')





#list_size = int(input("Enter the number of sub list "))

#print("\n")
#guessed_letters = [(input("Enter guess: "))]
#print(guessed_letters)

while True:
    guessed_letters = [(input("Enter guess: "))]
    if guessed_letters == 'stop': break
    print(guessed_letters)