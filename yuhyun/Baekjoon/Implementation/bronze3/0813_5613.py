result = int(input())
while True:
    cal = input()
    
    if cal == '=':
        break

    num = int(input())

    if cal == '+':
        result = result + num
    elif cal == '-':
        result = result - num
    elif cal == '*':
        result = result * num
    elif cal == '/':
        result = result // num # 소수점 버림

print(result)