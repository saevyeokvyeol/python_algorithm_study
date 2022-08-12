T = int(input())

for _ in range(T):
    n = int(input())
    a = b = 0
    pair = []

    if a + b == n :
        if a == b:
            break
        pair.append(f"{a} {b}")

    pair.sort()

        
    print(f"Pairs for {n}: ",end='')
    print(*pair)    

# 풀이 1
for _ in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}:", end=" ")
    result = []
    for i in range(1, n // 2 + 1):
        if n - i > 0 and i * 2 != n:
            result.append(f"{i} {n - i}")
    print(*result, sep=", ")

# 풀이 2
for _ in range(int(input())):
    n = int(input())
    result = [f"{i} {n - i}" for i in range(1, n // 2 + n % 2)]
    print(f"Pairs for {n}:", end=" ")
    print(*result, sep=", ")