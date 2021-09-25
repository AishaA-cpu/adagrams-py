import random


def dictionary_of_letters_to_tuple(dict):

    pool_of_letters_list = []

    for A, N in dict.items():
        while pool_of_letters_list.count(A) < N:
            pool_of_letters_list.append(A)

    tuple_of_letter_pool = tuple(pool_of_letters_list)

    return tuple_of_letter_pool

def draw_letters():

    LETTER_POOL = {
                'A': 9, 
                'B': 2, 
                'C': 2, 
                'D': 4, 
                'E': 12, 
                'F': 2, 
                'G': 3, 
                'H': 2, 
                'I': 9, 
                'J': 1, 
                'K': 1, 
                'L': 4, 
                'M': 2, 
                'N': 6, 
                'O': 8, 
                'P': 2, 
                'Q': 1, 
                'R': 6, 
                'S': 4, 
                'T': 6, 
                'U': 4, 
                'V': 2, 
                'W': 2, 
                'X': 1, 
                'Y': 2, 
                'Z': 1
                }

    pool_of_letters = dictionary_of_letters_to_tuple(LETTER_POOL)

    seq_of_letters = random.choices(pool_of_letters, k=10)
    
    for i in seq_of_letters:
        while seq_of_letters.count(i) > pool_of_letters.count(i):
            seq_of_letters = random.choices(pool_of_letters, k=10)

    return seq_of_letters



def uses_available_letters(word, letter_bank):
    try: 
        if not word.isupper():
            word = word.upper()
        
        for char in word:
            if char not in letter_bank or word.count(char) > letter_bank.count(char):
                return False
        return True 
    except ValueError:
        print("please enter alphabets")

def score_word(word):

    score = 0

    # score_chart = {
    #     1 : ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    #     2 : ["D", "G"],
    #     3 : ["B", "C", "M", "P"],
    #     4 : ["F", "H", "V", "W", "Y"],
    #     5 : ["K"],
    #     8 : ["J","X"],
    #     10 : ["Q", "Z"]
    # }

    # score_chart = {
    #     ("A", "E", "I", "O", "U", "L", "N", "R", "S", "T") : 1,
    #     ("D", "G") : 2,
    #     ("B", "C", "M", "P") : 3,
    #     ("F", "H", "V", "W", "Y") :4,
    #     ("K") : 5,
    #     ("J","X") : 8,
    #     ("Q", "Z") : 10

    # }

    score_chart = {"A": 1, 
        "E" : 1,
        "I" : 1,
        "O" : 1,
        "U" : 1, 
        "L" : 1, 
        "N" : 1, 
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3,
        "C" : 3,
        "M" : 3, 
        "P" : 3,
        "F" : 4, 
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8,
        "X" : 8,
        "Q" : 10,
        "Z" : 10,
    }

    word = word.upper()
    for char in word:
        score += score_chart[char]

    if len(word) >= 7:
        score += 8
    
    return score 

    # if not word.isupper():
    #         word = word.upper()

    # if word:
    #     for char in word:
    #         for point, list_of_letters in score_chart.items():
    #             if char in list_of_letters:
    #                 score += point
        
    #     if 7 <= len(word) <= 10:
    #         score += 8

    # letter_values = []
    # word = word.upper()
    # for char in word:
    #     for point, letter_list in score_chart.items():
    #         if char in letter_list:
    #             letter_values.append(point)
                
    # score = sum(letter_values)
    # if 7 <= len(word) <= 10:
    #     score += 8

    # return score








def get_highest_word_score(word_list):
    pass