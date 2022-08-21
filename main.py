import random, string
from words import words

alphabet = set(string.ascii_uppercase)
used_letters = []
wordArr = []
word_list = []

filwords = list(filter(lambda x: len(x)>=6 and '_' not in x, words))

word = random.choice(filwords).upper()
print(len(word))
print(word)

def split(word):
    wordArr =  [char for char in word]
    return wordArr

print(split(word))
lives = len(word)
print('you have received' ,lives, 'lives, lets play!!')
print('')


def hangman():
    global lives, word_list
    while lives!=0 :
        lives = lives - 1

        user_letter = input('Insert a letter: ').upper()
        if user_letter in alphabet:
            if user_letter in used_letters:
                print('you have already used this character, try again')
                print('you have remained' ,lives, 'lives, lets continue!!')
                print('')
            else:
                used_letters.append(user_letter)
                print('You have use these letters: ',' ' .join(used_letters))
                print('you have remained' ,lives, 'lives, lets continue!!')

                if user_letter in word:
                    word_list = [letter if letter in used_letters else '-' for letter in word]
                    print('Current word: ','' .join(word_list))
                    print('')

                else:
                    print('Try again!!')
                    print('')
        else:
            print('Enter valid english letter!!')

    if '-' not in word_list:
        print('you gussed the word,',word_list,'correctly.')
        print('***win********win*********win********win*********win***')

    elif lives == 0 and '-' in word_list:
        print('oh sorry, you are dead.')
        print('***Death********Death*********Death***')
   
hangman()
 


