import random

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

def dictionary_of_letters_to_tuple():

    pool_of_letters_list = []

    for A, N in LETTER_POOL.items():
        while pool_of_letters_list.count(A) < N:
            pool_of_letters_list.append(A)

    tuple_of_letter_pool = tuple(pool_of_letters_list)

    return tuple_of_letter_pool

def draw_letters():
    # pool_of_letters = ('A',
    #                     'A',
    #                     'A',
    #                     'A',
    #                     'A',
    #                     'A',
    #                     'A',
    #                     'A',
    #                     'A',
    #                     'B',
    #                     'B',
    #                     'C',
    #                     'C',
    #                     'D',
    #                     'D',
    #                     'D',
    #                     'D',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'E',
    #                     'F',
    #                     'F',
    #                     'G',
    #                     'G',
    #                     'G',
    #                     'H',
    #                     'H',
    #                     'I',
    #                     'I',
    #                     'I',
    #                     'I',
    #                     'I',
    #                     'I',
    #                     'I',
    #                     'I',
    #                     'I',
    #                     'J',
    #                     'K',
    #                     'L',
    #                     'L',
    #                     'L',
    #                     'L',
    #                     'M',
    #                     'M',
    #                     'N',
    #                     'N',
    #                     'N',
    #                     'N',
    #                     'N',
    #                     'N',
    #                     'O',
    #                     'O',
    #                     'O',
    #                     'O',
    #                     'O',
    #                     'O',
    #                     'O',
    #                     'O',
    #                     'P',
    #                     'P',
    #                     'Q',
    #                     'R',
    #                     'R',
    #                     'R',
    #                     'R',
    #                     'R',
    #                     'R',
    #                     'S',
    #                     'S',
    #                     'S',
    #                     'S',
    #                     'T',
    #                     'T',
    #                     'T',
    #                     'T',
    #                     'T',
    #                     'T',
    #                     'U',
    #                     'U',
    #                     'U',
    #                     'U',
    #                     'V',
    #                     'V',
    #                     'W',
    #                     'W',
    #                     'X',
    #                     'Y',
    #                     'Y',
    #                     'Z')

    pool_of_letters = dictionary_of_letters_to_tuple()

    seq_of_letters = random.choices(pool_of_letters, k=10)
    for i in seq_of_letters:
        while seq_of_letters.count(i) > pool_of_letters.count(i):
            seq_of_letters = random.choices(pool_of_letters, k=10)

    return seq_of_letters

    

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass