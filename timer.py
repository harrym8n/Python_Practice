import time

def countdown_timer():
    setting_time = int(input("타이머를 시작할 시간(초)을 입력하세요: "))

    print("타이머 시작!")

    print(setting_time)
    while setting_time > 0:
      setting_time -= 1
      time.sleep(1)
      print(setting_time)

    print("타이머 종료!")

#실행
countdown_timer()