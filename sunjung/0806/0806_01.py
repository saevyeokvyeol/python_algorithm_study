def solution(s):
    answer = 0
    s = []
    s = list(input())
    for i in range (len(s)+1) : #1~
        if s[i] == s[i+1] and s[i+1] == s[i+2] :
            print (s[i])
