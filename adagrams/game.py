import random

def draw_letters():
    pool_of_letters = ('A',
                        'A',
                        'A',
                        'A',
                        'A',
                        'A',
                        'A',
                        'A',
                        'A',
                        'B',
                        'B',
                        'C',
                        'C',
                        'D',
                        'D',
                        'D',
                        'D',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'E',
                        'F',
                        'F',
                        'G',
                        'G',
                        'G',
                        'H',
                        'H',
                        'I',
                        'I',
                        'I',
                        'I',
                        'I',
                        'I',
                        'I',
                        'I',
                        'I',
                        'J',
                        'K',
                        'L',
                        'L',
                        'L',
                        'L',
                        'M',
                        'M',
                        'N',
                        'N',
                        'N',
                        'N',
                        'N',
                        'N',
                        'O',
                        'O',
                        'O',
                        'O',
                        'O',
                        'O',
                        'O',
                        'O',
                        'P',
                        'P',
                        'Q',
                        'R',
                        'R',
                        'R',
                        'R',
                        'R',
                        'R',
                        'S',
                        'S',
                        'S',
                        'S',
                        'T',
                        'T',
                        'T',
                        'T',
                        'T',
                        'T',
                        'U',
                        'U',
                        'U',
                        'U',
                        'V',
                        'V',
                        'W',
                        'W',
                        'X',
                        'Y',
                        'Y',
                        'Z')


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