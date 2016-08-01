def isPower(A):
    if A == 1:
        return True
    if A < 3:
        return False
    to_check_till = int(A**0.5) + 1
    is_i_base = False
    for i in range(2,to_check_till):
        copy_A = A
        is_i_base = True
        while copy_A != 0:
            # print(copy_A, i)
            if copy_A == i:
                break
            if copy_A%i == 0:
                copy_A = copy_A // i
            else:
                print(copy_A, i)
                is_i_base = False
                break
        if is_i_base:
            break
    return is_i_base


A = 536870912
print(isPower(A))