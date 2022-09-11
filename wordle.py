import random

def main():
    possible_words = []
    f = open("sgb-words.txt",'r')
    for line in f:
        possible_words.append(line.strip())
    word = random.choice(possible_words)

    guesses = 0
    print("Enter a 5 letter word")
    user_guess = ''
    while user_guess != word:
        user_guess = input()
        while user_guess not in possible_words:
            user_guess = input("Enter a valid 5 letter word\n")
        clues = ''

        for i in range(5):
            if user_guess[i] == word[i]:
                clues += '🟩'
            elif user_guess[i] in word:
                clues += '🟨'
            else:
                clues += '⬜'
        print(clues)
        guesses += 1
    print(str(guesses) + " guesses\n")
main()
    