import random
from hangman_words import words
from hangman_stages import stages
print("Welcome to my hangsman game!!")
name=input("What is your name?")
print(f"Nice to meet you {name}.Let's begin!!")
health=6
random_index=random.randint(0,563)
chosen_word=list(words[random_index])
length_of_word=len(chosen_word)
blank_list=[]
for character in range(length_of_word):
    blank_list.append('_')

word=''.join(blank_list)
word_as_list=list(word)
word=' '.join(word_as_list)
wrong_guesses=[]
true_guesses=[]

while '_' in word:
    if health==0:
        print("You lose,please try again!")
    letter=input("Enter a letter: ").lower()
    while letter in true_guesses:
        letter=input("You already found this letter,try new one.")
    while letter in wrong_guesses:
        letter=input("You already try this letter,try new one.")
    if letter in chosen_word:
        true_guesses.append(letter)
        for index,char in enumerate(chosen_word):
            if char == letter:
                word_as_list[index]=letter
                word=' '.join(word_as_list)

                if '_' not in word:
                    print("YOU WİNN!!")
                    quit()
        print("Congratulations!You find a letter!!")
        print(stages[health])
        print(word)

    else:
        wrong_guesses.append(letter)
        health -= 1
        if health==0:
            chosen_word_str="".join(chosen_word)
            print(stages[health])
            print(f"You lose,word was '{chosen_word_str}'.Please try again!")
            break
        print("Sorry,keep going on!")
        print(stages[health])
        print(word)


