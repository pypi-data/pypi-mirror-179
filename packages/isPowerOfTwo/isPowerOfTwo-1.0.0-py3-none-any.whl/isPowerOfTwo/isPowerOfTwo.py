def isPowerOfTwo(n):
    if n <= 0:
        return False
    # Convert n to binary
    n1 = bin(n)[2:]
    n2 = bin(n-1)[2:]
    # Perform bitwise AND operation
    n3 = int(n1, 2) & int(n2, 2)
    # If the result is 0, then n is a power of 2
    if n3 == 0:
        return True
    return False