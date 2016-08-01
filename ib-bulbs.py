def bulbs(A):
    count = 0
    for i in A:
        if count % 2 == 0:
            current = i
        else:
            current = abs(i-1)
        if current == 0:
            count += 1
    return count


A = [0,1,0,1]
A = [0,1,1,1]
print(bulbs(A))