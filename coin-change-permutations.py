import copy
from pprint import pprint

denominations = [25, 10, 5, 1]
results = []

def find_permutations_change(n, sol, starting_point):
    sum = 0
    if n < 0:
        return 0
    if n == 0:
        print('sol - ', sol)
        return 1
    for i in denominations:
        if i <= starting_point:
            sol.append(i)
            subset = find_permutations_change(n-i, sol[:], i)
            sum += subset
            sol.pop()
    return sum

def permutations(n, arr):
    if n == 0 or len(arr) == 1:
        return 1
    current = arr[0]
    arr.remove(arr[0])
    sum = 0
    while n >= 0:
        brr = arr[:]
        current_sum = permutations(n, brr)
        sum += current_sum
        n = n - current
    return sum

print(find_permutations_change(25, [], denominations[0]))
print(permutations(25, [25,10,5,1]))
# print(permutations(50, [10,5,1]))
# print(permutations(75, [10,5,1]))
# print(permutations(100, [10,5,1]))
