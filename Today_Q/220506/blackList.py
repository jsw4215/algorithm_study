from itertools import permutations 

def checkFunc(id, ban_id):

    for i in range(len(id)):
        for j in range(len(id[i])):
            if len(id[i])!=len(ban_id[i]):
                return False

            if ban_id[i][j]=="*":
                continue
            if id[i][j]!=ban_id[i][j]:
                return False

    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))

    res = []
    for names in user_permutation:
        if not checkFunc(names,banned_id):
            continue
        else:
            names = set(names)
            if names not in res:
                res.append(names)
    return len(res)

if __name__ == '__main__':

    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    res = solution(user_id, banned_id)
    print(res)
    