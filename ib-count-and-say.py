def countAndSay(A):
    if A == 1:
        return '1'

    old = "11"
    new = ""
    for j in range(1,A-1):
        count = 1
        for i in range(1,len(old)):
            if old[i] == old[i-1]:
                count += 1
            else:
                new += str(count) + old[i-1]
                count = 1
        new += str(count) + old[-1]

        old = new[:]
        new = ""
        # print(old)
    return old



A = 5
print(countAndSay(A))