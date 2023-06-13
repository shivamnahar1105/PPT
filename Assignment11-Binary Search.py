# Q1.
def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

