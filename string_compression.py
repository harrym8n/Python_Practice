# 문제
def compress_string(s):
  result = []
  prev_char = s[0]
  result.append((0, prev_char))

  for i in range(1, len(s)):
    if s[i] != prev_char:
      result.append((i, s[i]))
      prev_char = s[i]

  new_s = ""
  for i in range(1,len(result)+1):
    if i != len(result):
      new_num = result[i][0] - result[i-1][0]
    else:
      new_num = len(s) - result[i-1][0]

    new_s = new_s + f"{result[i-1][1]}{new_num}"

  if len(new_s) < len(s):
    return new_s
  else:
    return s



# 프로그램 실행
compress_string("aabcccccaaa")