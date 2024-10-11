"""
import random
#정답 생성
answer = random.randint(1, 20)
print(answer)


#게임 생성
user_answer = int(input(f"기회가 4번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
if user_answer != answer:
    if user_answer > answer:
        print("Down")
    elif user_answer < answer:
        print("Up")
    for i in range(4) :
        if i < 3 and user_answer != answer:
            user_answer = int(input(f"기회가 {3-i}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
            if user_answer > answer :
                print("Down")
            elif user_answer < answer :
                print("Up")
        elif i == 3 and user_answer != answer :
            print(f"아쉽습니다. 정답은 {answer}였습니다.")
        else:
            print(f"축하합니다. {i+1}번만에 숫자를 맞히셨습니다.")
            break
else :
    print(f"축하합니다. 1번만에 숫자를 맞히셨습니다.")
"""
#랜덤 모듈 임포트
import random

#상수 정의
ANSWER = random.randint(1,20)
NUM_TRIES = 4

#변수 정의
guess = -1
tries = 0

#게임 생성
while guess != ANSWER and NUM_TRIES > tries :
    guess = int(input(f"기회가 {(NUM_TRIES - tries)}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
    tries += 1

    if ANSWER > guess:
        print("UP")
    elif ANSWER < guess:
        print("DOWN")

if guess == ANSWER:
    print(f"축하합니다. {tries}번 만에 숫자를 맞히셨습니다.")
else:
    print(f"아쉽습니다. 정답은 {ANSWER}입니다.")