a = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]


def print_single_spiral(a, r_start, r_stop, c_start, c_stop, result):
    if r_start > r_stop or c_start > c_stop:
        return result
    if r_start == r_stop and c_start == c_stop:
        result.append(a[r_start][c_start])
        return result
    elif r_start == r_stop:
        for i in range(c_start,c_stop+1):
            result.append(a[r_start][i])
        return result
    elif c_start == c_stop:
        for i in range(r_start,r_stop+1):
            result.append(a[i][c_start])
        return result
    else:
        for i in range(c_start,c_stop):
            result.append(a[r_start][i])
        for i in range(r_start,r_stop):
            result.append(a[i][c_stop])
        for i in range(c_stop,c_start,-1):
            result.append(a[r_stop][i])
        for i in range(r_stop,r_start,-1):
            result.append(a[i][c_start])
        print(r_start+1, r_stop-1, c_start+1, c_stop-1, result)
        return print_single_spiral(a, r_start+1, r_stop-1, c_start+1, c_stop-1, result)



print(print_single_spiral(a,0,len(a)-1, 0, len(a[0])-1, []))