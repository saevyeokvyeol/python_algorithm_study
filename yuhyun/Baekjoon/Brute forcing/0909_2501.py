n, k = map(int, input().split())
divisor = []

for i in range(1,n+1):

    if n % i == 0:
        divisor.append(i)

print(divisor[k-1] if len(divisor) >= k else 0)
