#<평균 구하기>
#방법 1
def solution(arr):
    sum = 0
    count = 0
    
    for num in arr:
        sum += num
        count += 1
        
    return sum / count

#방법 2
def solution(arr):
    return sum(arr) / len(arr)

#<x만큼 간격이 있는 n개의 숫자>
def solution(x, n):
    answer = []
    plus = x
    
    while len(answer) < n:
        answer.append(x)
        x += plus
        
    return answer

#<짝수와 홀수 구분하기>
def solution(num:int):
    if num % 2 == 0:
        answer = "Even"
    else :
        answer = "Odd"
    
    return answer


#<신규 아이디 추천>
import string

def solution(new_id):
    answer = ''
    
    # 1단계
    answer = new_id.lower()  

    # 2단계
    symbols = string.punctuation.replace('-', '').replace('_', '').replace('.', '')
    for symbol in symbols:
        answer = answer.replace(symbol,'')

    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    answer = answer.strip('.')

    # 5단계
    if answer == '':
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]

        while answer[-1] == '.':
            answer = answer.rstrip('.')

    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer
