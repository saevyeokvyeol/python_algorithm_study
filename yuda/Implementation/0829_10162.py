n = int(input())
if n % 10:
    print(-1)
else:
    print(n // 300, n % 300 // 60, n % 60 // 10)