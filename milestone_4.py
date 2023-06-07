import random
#%% task 1
class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.num_letters = len(self.word)
        self.word_guessed  = [' ']*self.num_letters
        self.list_of_guesses = []

#%% create method to run the checks
self_word = ['apple']
self_list_of_guesses=[]
num_letters = 5
word_guessed = ['']*5
num_lives = 5

def check_guess(guess, num_letters, num_lives):
    self_guess = guess.lower()
    listed_self_word = list(self_word[0])
    if self_guess in listed_self_word:
        print(f'Good guess! {guess} is in the word.')
        for idx in range(len(listed_self_word)):
            if self_guess == listed_self_word[idx]:
                word_guessed[idx] = self_guess
        num_letters += -1
        print(word_guessed)
    else: 
        num_lives -= 1
        print(f'Sorry, {guess} is not in the word')
        print(f'You have {num_lives} lives left')
    return word_guessed

def ask_for_input():
    while True:
        guess = input('Enter a letter')
        if not guess.isalpha() or len(guess) != 1:
            print('Invalid letter. Please, enter a single alphabetic character.')
        elif guess in self_list_of_guesses:
            print('You have already tried this letter!')
        else:
            check_guess(guess, num_letters, num_lives)
            self_list_of_guesses.append(guess)

# %%
user_guessed = ask_for_input()
# %%
