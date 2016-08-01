def sqrt(A):
    lo = 0
    hi = A

    if A < 1:
        return 0
    if A == 1:
        return 1

    while hi > lo:

        mid = (hi+lo)//2
        square = mid*mid

        # print(mid)
        if square == A:
            return mid
        elif A > (mid - 1)**2 and A < mid**2:
            return mid - 1
        elif A > mid**2 and A < (mid + 1)**2:
            return mid
        elif square > A:
            hi = mid
        elif square < A:
            lo = mid


A = 10
print(sqrt(A))
