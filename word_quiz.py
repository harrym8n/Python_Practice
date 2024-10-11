import random
#내 풀이
with open("vocabulary.txt", 'r') as f:
    random_english = {}
    for line in f:
        #문제 출제 및 사용자 답변 받기
        data = line.strip().split(': ')

        #변수 지정
        english_word = data[0]
        korean_word = data[1]

        #영어 단어 사전 생성
        random_english[english_word] = korean_word
    while True:
        #문제와 답 생성
        question = random.choice(list(random_english.keys()))
        answer = random_english[question]

        #영어 단어 리스트에서 랜덤 추출하여 문제 내기
        user_answer = input(f"{question}: ")

        #종료 프로세스
        if user_answer == "q":
            break

        #정답 판별
        if user_answer == answer:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {answer}입니다.")
"""
#해설 풀이
with open("vocabulary.txt", 'r') as f:
    random_english = {}
    for line in f:
        # 문제 출제 및 사용자 답변 받기
        data = line.strip().split(': ')

        # 변수 지정
        english_word = data[0]
        korean_word = data[1]

        # 영어 단어 사전 생성
        random_english[english_word] = korean_word

        # 문제와 답 생성
        # 영어 단어 리스트 생성
        keys = list(random_english.keys())

    while True:
        # 랜덤 인덱스 생성
        index = random.randint(0, len(keys) - 1)

        # 영어 단어 리스트에서 랜덤 추출하여 문제 내기
        user_answer = input(f"{keys[index]}: ")
        answer = random_english[keys[index]]  # 문제의 답

        if user_answer == 'q':
            break

        # 정답 판별
        if user_answer == answer:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {answer}입니다.")
"""