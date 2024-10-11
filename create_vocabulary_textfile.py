#파일 생성하기
with open("vocabulary.txt",'w') as f:
    #변수 선언
    english = "test"
    korean = "테스트"
    #단어 입력하기(인풋 받기)
    while  english != "q":
        english = input("영어 단어를 입력하세요:")
        korean = input("한국어 뜻을 입력하세요:")
        #종료 프로세스 추가하기
        if english == "q":
            break
        elif korean == "q":
            break
    #받은 인풋 파일에 추가하기
        f.write(english + ": ")
        f.write(korean + "\n")
