def add_single(a, b, carry):
    if b == '':
        int_a = int(a)
        sum = int_a + carry
    else:
        int_a, int_b = int(a), int(b)
        sum = int_a + int_b + carry
    value = sum % 2
    new_carry = sum // 2
    return new_carry, value



def addBinary(A, B):
    result = ''
    carry = 0
    bigger = ''
    bigger_len = 0
    len_min = min(len(A), len(B))
    len_A = len(A)
    len_B = len(B)
    if len_A > len_B:
        bigger = A
        bigger_len = len_A
    elif len_B > len_A:
        bigger = B
        bigger_len = len_B

    for i in range(0,len_min):
        carry, value = add_single(A[len_A - i - 1], B[len_B - i - 1], carry)
        result  = str(value) + result

    if bigger != '':
        for i in range(len_min, bigger_len):
            carry, value = add_single(bigger[bigger_len - i - 1], '', carry)
            result  = str(value) + result

    if carry == 1:
        result = '1' + result

    return result

A = '101'
B = '111'

print(addBinary(A, B))