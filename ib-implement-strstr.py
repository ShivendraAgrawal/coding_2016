def strStr(haystack, needle):
    len_needle = len(needle)
    if len_needle == 0:
        return -1
    i, j = 0, 0
    while(i < len(haystack)):
        if haystack[i] == needle[j]:
            j += 1
            if j == len_needle:
                return i - len_needle + 1
        else:
            i = i - j
            j = 0
        i += 1

    return -1

A = 'bbbbbbbbaba'
B= 'baba'
A = 'aabaaaababaabbbabbabbbaabababaaaaaababaaabbabbabbabbaaaabbbbbbaabbabbbbbabababbaaabbaabbbababbb'
B = 'bba'
# A = 'abbaabaaaaabbabbaabbbabbbbbaabbaabbabaaabaaaaaabaabbaabbaabbbaaaaaaaabaabbbbaabaaabbbbaaaaa'
# B = 'babbabbbbbbabaabbaaabaaaabbaaaabb'
print(strStr(A,B))