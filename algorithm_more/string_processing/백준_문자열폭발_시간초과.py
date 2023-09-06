# 문자열 폭발
# 폭발 문자열이 폭발 -> 그 문자 문자열에서 사라지고 남은 문자끼리 합쳐진다
# 문자열에 폭발 문자열 있을 경우, 모든 폭발 문자열이 폭발, 새로 문자열을 만든다
# 새로생긴 문자열에도 폭발문자열이 있을 수 있다
# 폭발문자열이 끝나고 남은 문자열을 출력하는데 , 남은 문자열이 없으면 FRULA 를 출력

def bomb_after(test_string, bomb_string):
    if test_string =='':
        return 'FRULA' 
    after_string= test_string.replace(bomb_string, '')
    if after_string == test_string:
        return after_string
    else:
        return bomb_after(after_string, bomb_string)

test_string = input()
bomb_string = input()

print(bomb_after(test_string, bomb_string))