from pprint import pprint

def findLongestPalindrome(A):
    len_A = len(A)
    dp = [True for row in range(0, len_A)]
    max_length = 1
    max_i, max_j = 0, 0

    dp_2 = [False for row in range(0, len_A)]
    for i in range(0, len_A-1):
        if A[i] == A[i+1]:
            dp_2[i] = True
            length = 2
            if length > max_length:
                max_length = length
                max_i = i
                max_j = i+1


    for j in range(2, len_A):
        i = 0
        while i+j < len_A:
            # print(dp[i][j+i])

            if j%2 == 0 :
                if dp[i+1] == True and A[i] == A[j+i]:
                    dp[i] = True

                    # print(A[i:i+j+1], (i,j), i, (A[i], A[j+i]))

                    length = j+1
                    if length > max_length:
                        max_length = length
                        max_i = i
                        max_j = j+i
                else:
                    dp[i] = False
            else:
                if dp_2[i+1] == True and A[i] == A[j+i]:
                    dp_2[i] = True

                    # print(A[i:i+j+1], (i,j), i, (A[i], A[j+i]))

                    length = j+1
                    if length > max_length:
                        max_length = length
                        max_i = i
                        max_j = j+i
                else:
                    dp_2[i] = False
            i += 1

    return A[max_i: max_j+1]



A = 'abcddcabacdefghihj'
A = 'abb'
A = 'caccbcbaabacabaccacaaccaccaaccbbcbcbbaacabccbcccbbacbbacbccaccaacaccbbcc'
print(findLongestPalindrome(A))