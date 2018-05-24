def isPowerOfTwo(n):
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
    return True
if(isPowerOfTwo(64)):
    print('Yes')
else:
    print('No')
