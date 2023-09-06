from itertools import permutations
def check (users, banned_id) :
    for i in range (len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False
        for j in range(len(users[i])):
            if banned_id[i][j] == '*' : 
                continue
            else:
                if users[i][j] != banned_id[i][j]:
                    return False
    return True

def solution(user_id, banned_id) :
    user_able = list(permutations(user_id, len(banned_id)))
    # 여기도 포인트 순열을 사용할때는 어떻게 해서 다른 경우로 치나 결과가 같을 수 있으므로 set을 잘 사용해야함
    ban_set=[]
    for users in user_able:
        if not check(users, banned_id):  # 불가능한 조합이면
            continue 
        else:
            # 가능한 조합이더라도 ban_set에 넣고 set을 사용해야한다.
            users = set(users) # 순서 1,2,3 /3,2,1 이더라도 같게 하기 위해서 
            if users not in ban_set:
                ban_set.append(users)
    return len(ban_set)