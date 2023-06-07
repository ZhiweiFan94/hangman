import random

word_list = ["apple", "banana", "orange", "grape", "watermelon"]
random_word = random.choice(word_list)

#%% task 1
def ask_for_input():
    while True:
        guess = input()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)
# %% task 2
def check_guess(user_letter):
    guess = user_letter.lower()
    if guess in random_word:
        print(f'Good guess! {guess} is in the word')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
# %%
ask_for_input()