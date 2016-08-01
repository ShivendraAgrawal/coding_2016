def lengthOfLastWord(A):
    A = A.strip()
    if len(A) == 0:
        return 0
    index_space = -1
    for i in range(len(A)-1, 0, -1):
        if A[i] == " ":
            index_space = i
            break
    if index_space == -1:
        return len(A)
    return len(A[index_space+1:])

s = "Hello World"
print(lengthOfLastWord(s))