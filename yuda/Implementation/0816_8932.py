S = [[9.23076, 26.7, 1.835], [1.84523, 75, 1.348], [56.0211, 1.5, 1.05], [4.99087, 42.5, 1.81], [0.188807, 210, 1.41], [15.9803, 3.8, 1.04], [0.11193, 254, 1.88]]
for _ in range(int(input())):
    n = list(map(int, input().split()))
    score = 0
    for i in range(len(S)):
        if i % 3 == 0:
            score += int(S[i][0] * ((S[i][1] - n[i]) ** S[i][2]))
        else:
            score += int(S[i][0] * ((n[i] - S[i][1]) ** S[i][2]))
    print(score)