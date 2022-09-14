

from numpy import short

def getClues(guess, word):
    clues = ""
    for i in range(5):
            if guess[i] == word[i]:
                clues += '3' #'🟩'
            elif guess[i] in word:
                clues += '2' #'🟨'
            else:
                clues += '1' #'⬜'
    return clues

def isValid(word, green, yellow, white):
    for i in range(len(green)):
        if green[i] != "?" and green[i] != word[i]:
            return False
    
    for i in yellow:
        if i not in word:
            return False

    for i in white:
        if i in word:
            return False
    
    return True

def shorten_list(green, yellow, white, possible_words):
    new_list = []
    for i in possible_words:
        if isValid(i, green, yellow, white):
            new_list.append(i)
    return new_list
        

def find_best_word(green, yellow, white, possible_words):
    best_word = ""
    best_count = 0
    for possible_best in possible_words:
        print(possible_best)
        average_removed_sum = 0
        for possible_solution in possible_words:
            total_removed = 0
            new_g = green
            new_y = list(yellow)
            new_w = list(white)
            result = getClues(possible_best, possible_solution)
            for i in range(5):
                if result[i] == "3":
                    new_g[i] = possible_best[i]
                elif result[i] == "2":
                    new_y.append(possible_best[i])
                elif result[i] == "1":
                    new_w.append(possible_best[i])

            for w in possible_words:
                if not isValid(w, new_g, new_y, new_w):
                    total_removed += 1
            average_removed_sum += total_removed/len(possible_words)
        if best_word == "" or average_removed_sum > best_count:
            best_word = possible_best
            best_count = average_removed_sum
        print(average_removed_sum/len(possible_words))
    return best_word

    



def solver():
    green = ["?","?","?","?","?"]
    yellow = []
    white = []

    possible_words = []
    f = open("sgb-words.txt",'r')
    for line in f:
        possible_words.append(line.strip())

    solved = False
    best_word = "stare"
    result = ""

    while not solved:
        possible_words = shorten_list(green, yellow, white, possible_words)
        best_word = find_best_word(green, yellow, white, possible_words)
        print("Your best word is " + best_word)
        result = input("Type in Results: \n")
        while len(result) != 5:
            result = input("Type in valid results: \n")
        
        if result == "33333":
            solved = True
        
        for i in range(len(result)):
            if result[i] == "3":
                green[i] = best_word[i]
            elif result[i] == "2":
                yellow.append(best_word[i])
            elif result[i] == "1":
                white.append(best_word[i])
        

solver()