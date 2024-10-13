from random import randint

#답 생성
def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        number = randint(0, 9)
        if number not in numbers:
            numbers.append(number)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


#숫자 예측하기
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    n = 1

    while len(new_guess) < 3:
        guess = int(input(f"{n}번째 숫자를 입력하세요: "))
        if guess > 9 or guess < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        elif guess in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue

        new_guess.append(guess)
        n += 1

    return new_guess


#점수 계산
def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guesses[i] == solution[i]:
            strike_count += 1
        elif guesses[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    guesses = take_guess()
    tries += 1

    s, b = get_score(guesses, ANSWER)
    print(f"{s}S {b}B")

    if s == 3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))
