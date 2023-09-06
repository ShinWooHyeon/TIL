test_string = input()
bomb_string = input()
stack = []
bomb_len = len(bomb_string)
for i in range(len(test_string)):
    # 앞 뒤 문자열폭발을 동시에 진행하는게 아니라 앞에서부터 차차근 제거한다 
    stack.append(test_string[i])
    # 확인한 문자열에서부터 폭발문자열의 길이만큼 확인한 것이 폭발문자열이라면 폭발문자열 길이만큼 pop 해야한다
    # 이게 조금 어려울 수 있는데 stack에서 뒤에서부터 폭발문자열의 길이만큼 확인한다 
    if ''.join(stack[-1 * bomb_len:]) == bomb_string:
        for _ in range (bomb_len):
            stack.pop()

after_string = ''.join(stack)
if after_string:
    print(after_string)
else:
    print('FRULA')