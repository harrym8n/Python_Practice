# 문제
def add_numbers():
  while True:
    try :
      num1 = int(input("첫 번째 숫자를 입력하세요: "))
      break
    except:
      print("올바른 숫자를 입력하세요.")

  while True:
    try :
      num2 = int(input("두 번째 숫자를 입력하세요: "))
      break
    except:
      print("올바른 숫자를 입력하세요.")

  return f"{num1} + {num2} = {num1+num2}"



# 프로그램 실행
add_numbers()