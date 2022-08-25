def solution(K, words):
    answer = 1
    i = len(words[0])
    for word in words[1:]:
        if i + len(word) + 1 <= K:
            i += len(word) + 1
        else:
            answer += 1
            i = len(word)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")