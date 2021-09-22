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
    
    word = word.upper()
    
    for char in word:
        if char not in letter_bank or word.count(char) > letter_bank.count(char):
            return False
    return True   

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass