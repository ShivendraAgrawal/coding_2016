A = 'AB'

def find_column_number(A):
    number = 0
    for i, char in enumerate(reversed(A.lower())):
        rank_char = ord(char) - 96
        number += rank_char * (26**i)
    return number

print(find_column_number(A))