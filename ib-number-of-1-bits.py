def num_to_bin(k):
    result  = 0
    while(k != 1):
        result += k % 2
        k = k // 2
    if k == 1:
        return result + 1
    return result

print(num_to_bin(7))
