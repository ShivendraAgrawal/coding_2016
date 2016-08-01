def print_matrix(matrix):
    for row in matrix:
        for j in row:
            print(j)
        print
    print

input_matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]

print_matrix(input_matrix)

def swap(i, j, n, matrix):
    first_time = True
    from_i = i
    from_j = j
    to_i = from_j
    to_j = n - from_i - 1
    from_value  = matrix[from_i][from_j]
    to_value = None

    while( not(from_i == i and from_j == j) or first_time):
        to_value = matrix[to_i][to_j]
        matrix[to_i][to_j] = from_value
        from_value = to_value
        from_i = to_i
        from_j = to_j

        to_i = from_j
        to_j = n - from_i - 1
        first_time = False

def rotate_matrix(matrix):
    n = len(matrix)
    mid = int(n/2)
    start = 0
    stop = n - 1
    for i in range(mid):
        for j in range(start, stop):
            swap(i, j, n, matrix)
        start+=1
        stop-=1
    print_matrix(matrix)


rotate_matrix(input_matrix)