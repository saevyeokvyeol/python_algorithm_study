for _ in range(int(input())):
    n, t = map(int, input().split())
    b = bin(n)[2:].count('1') # n = str(format(n,'b'))
    print("Valid" if int(b)%2 == t else "Corrupt")