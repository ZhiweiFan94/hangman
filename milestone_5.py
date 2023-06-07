#%% task 1
import random
class Hangman:
    def __init__(self, word_list, num_lives=5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.num_letters = len(list(self.word))
        self.word_guessed  = ['']*self.num_letters
        self.list_of_guesses = []
        # print(self.word + ' ' + str(self.num_letters))

    def check_guess(self, guess):
        # print(f'check_{self.word}')
        self_guess = guess.lower()
        listed_self_word = list(self.word)
        if self_guess in listed_self_word:
            print(f'Good guess! {guess} is in the word.')
            for idx in range(len(listed_self_word)):
                if self_guess == listed_self_word[idx]:
                    self.word_guessed[idx] = self_guess
                    self.num_letters -= 1
            print(self.word_guessed)
        else: 
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
        # return self.num_letters, self.num_lives

    def ask_for_input(self):
        while True:
            guess = input('Enter a letter')
            if not guess.isalpha() or len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetic character.')
            elif guess in self.list_of_guesses:
                print('You have already tried this letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            # print(f'numletter{self.num_letters} and numlive{self.num_lives}')
            return self.num_letters, self.num_lives


#%% excute the game
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:    
        if num_lives == 0:
            print('You lost!')
            break
        elif num_lives > 0:
            num_letters, num_lives = game.ask_for_input()
            if num_lives != 0 and num_letters == 0:
                print('Congratulations. You won the game!')
                break

play_game(word_list=['apple','orange','watermelon','lemon','grape']) 


# %%
