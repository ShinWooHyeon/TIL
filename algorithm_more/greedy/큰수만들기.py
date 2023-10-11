def solution(number, k):
    answer = [] # Stack
    # answer에 붙이고 answer이 비어있지 않고 맨마지막 숫자가 num보다 
    # answer에 숫자 붙이고(비어있지않을때) 그 다음숫자가 answer 마지막보다 크면 빼고 그 숫자 넣는다
    # for문이 안돌아가므로 k번 빠진  len(number) -
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])