def solution(survey, choices):
    #점수 환산
    types = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

    res = ''

    for i in range(len(choices)):
        ans = choices[i]-4
        if ans>0:
            types[survey[i][1]] += ans
        elif ans<0:
            types[survey[i][0]] += abs(ans)
    
    if types['R']>=types['T']:
        res+='R'
    else:
        res+='T'

    if types['C']>=types['F']:
        res+='C'
    else:
        res+='F'

    if types['J']>=types['M']:
        res+='J'
    else:
        res+='M'

    if types['A']>=types['N']:
        res+='A'
    else:
        res+='N'

    return res

if __name__ == '__main__':

    survey = ["AN", "CF", "MJ", "RT", "NA"]
    choices = [5, 3, 2, 7, 5]

    res = solution(survey, choices)

    print(res)