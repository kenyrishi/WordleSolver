

from numpy import short


def isValid(word, green, yellow, white):
    for i in green:
        if green[i] != "?" and green[i] != word[i]:
            return False
    
    for i in yellow:
        if yellow[i] not in word:
            return False

    for i in white:
        if white[i] in word:
            return False
    
    return True

def shorten_list(green, yellow, white, possible_words):
    new_list = []
    for i in possible_words:
        if isValid(i, green, yellow, white):
            new_list.append(i)
    return new_list
        

def find_best_word(green, yellow, white, possible_words):
    pass

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
        



