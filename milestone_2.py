# %% Task 1
word_list = ['apple','banana','orange','watermelon','lemon']
print(word_list)

# %% task 2
import random

word = random.choice(word_list)
print(word)

# %%task 3
guess = input('enter a single letter')


# %% task 4
if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Ooops! That is not a valid input.')


