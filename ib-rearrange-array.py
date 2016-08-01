def arrange_1(A):
    for i, ele in enumerate(A):
        if ele >=0:
            print(i,ele)
            index = i
            old_past_arr_i_value = A[index]
            arr_i_accessor = A.index(index)
            A[index] = -1*A[A[index]]

            while(A[arr_i_accessor] > 0):
                print(arr_i_accessor)
                print A
                new_past_arr_i_value = A[arr_i_accessor]
                A[arr_i_accessor] = -1*old_past_arr_i_value
                old_past_arr_i_value = new_past_arr_i_value
                arr_i_accessor = A.index(new_past_arr_i_value)

    return A

def arrange(A):
    len_A = len(A)
    for i, ele in enumerate(A):
        value = A[i] % len_A
        value_ception = A[value] % len_A
        print(value)
        A[i] += value_ception * len_A

    for i, ele in enumerate(A):
        A[i] = A[i] // len_A
    return A

A = [4,1,0,3,2]
print(arrange(A))