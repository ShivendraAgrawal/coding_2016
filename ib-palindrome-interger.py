A = 0

def is_integer_palindrome(A):
    if A < 0:
        return False
    list_A = []
    if A == 0:
        list_A.append(0)
    copy_A = A
    len_A = 0
    while(copy_A != 0):
        len_A += 1
        list_A.append(copy_A%10)
        copy_A = copy_A // 10

    to_check_till = len_A // 2
    for i in range(0, to_check_till+1):
        if list_A[i] != list_A[len_A - i - 1]:
            return False
    return True

print(is_integer_palindrome(A))