def colorful(A):
    all_muls = {}
    num_list = []
    while A > 0:
        num_list.append(A % 10)
        A = A // 10

    j = 1
    while j <= len(num_list):
        for i in range(0, len(num_list) - j + 1):
            mul = 1
            for k in range(i, i+j):
                mul *= num_list[k]
            # print(i,j ,k,mul)

            if mul in all_muls:
                # print(all_muls)
                return 0
            else:
                all_muls[mul] = 1
        j += 1

    return 1



A = 3245
print(colorful(A))