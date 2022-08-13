# 풀이 1
P = {"Wide Receiver":[4.5, 150, 200], "Lineman":[6.0, 300, 500], "Quarterback":[5.0, 200, 300]}

while True:
    N = list(map(float, input().split()))
    if sum(N) == 0:
        break
    
    position = list(P.keys())
    for k in P.keys():
        for i in range(len(P[k])):
            if i == 0:
                if N[i] > P[k][i]:
                    position.remove(k)
                continue
            if N[i] < P[k][i]:
                position.remove(k)
                break

    print(*position) if len(position) else print("No positions")

# 풀이 2
while True:
    sp, w, st = map(float, input().split())
    if (sp, w, st) == (0, 0, 0):
        break

    P = []
    if sp <= 4.5 and w >= 150 and st >= 200:
        P.append("Wide Receiver")
    if sp <= 6.0 and w >= 300 and st >= 500:
        P.append("Lineman")
    if sp <= 5.0 and w >= 200 and st >= 300:
        P.append("Quarterback")

    print(*P) if len(P) else print("No positions")