def power(x,n,d):
    if x == 0:
        return 0
    if n == 2:
        return ((x%d)*(x%d))%d
    if n == 1:
        return x%d
    if n == 0:
        return 1

    if n % 2 == 1:
        result = power(x, n//2, d)
        return ((result%d)*(result%d)*(x%d))%d
    else:
        result = power(x, n//2, d)
        return ((result%d)*(result%d))%d


x, n, d = 0, 0, 1

print(power(x, n, d))