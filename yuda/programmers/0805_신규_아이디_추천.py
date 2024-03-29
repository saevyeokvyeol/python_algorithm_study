import re

# 풀이 1
def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    check = list(new_id)
    string = [chr(i) for i in range(97, 97 + 26)]
    string.extend(list("-_.0123456789"))
    new_id = ""
    for s in check:
        if s in string:
            new_id += s

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while ".." in new_id:
        new_id = new_id.replace("..", ".")

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if new_id[0] == '.':
        new_id = new_id[1:]
    elif new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = "a"

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    new_id = new_id[0:15]

    #     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

def solution2(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    new_id = re.sub('[^0-9a-z\-_.]', '', new_id)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id = re.sub('\.+', '.', new_id)

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = re.sub('^[.]|[.]$', '', new_id)

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = "a"

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    new_id = new_id[0:15]

    #     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    new_id = re.sub('[.]$', '', new_id)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("abcdefghijklmn.p"))
print(solution2("...!@BaT#*..y.abcdefghijklm"))
print(solution2("z-+.^."))
print(solution2("=.="))
print(solution2("abcdefghijklmn.p"))