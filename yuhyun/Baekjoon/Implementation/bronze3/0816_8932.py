t = int(input())

for _ in range(t):
    lst = list(map(int, input().split()))

    sum = int(9.23076*(26.7-lst[0])**1.835) + int(1.84523*(lst[1]-75)**1.348) + int(56.0211*(lst[2]-1.5)**1.05) + int(4.99087*(42.5-lst[3])**1.81) + int(0.188807*(lst[4]-210)**1.41) + int(15.9803*(lst[5]-3.8)**1.04) + int(0.11193*(254-lst[6])**1.88)

    print(sum)