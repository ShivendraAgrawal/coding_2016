def atoi(A):
    A = A.strip()
    has_sign = False
    number_string = ''
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    for i,char in enumerate(A):
        if has_sign == False and (char =='+' or char == '-'):
            has_sign = True
        else:
            ascii_val = ord(char)
            if ascii_val >= 48 and ascii_val <= 57:
                end_index = i
                number_string += char
            else:
                break
    if len(number_string) == 0:
        return 0
    if has_sign:
        number_string = A[0] + number_string
    result = int(number_string)
    if result > INT_MAX:
        return INT_MAX
    if result < INT_MIN:
        return INT_MIN
    return result


A = "   -512.12 bottles of beer on the wall"
A = '93270412345'
print(atoi(A))