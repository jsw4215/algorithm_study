import sys

def solution(num_A_B, data):

    inRoomA = num_A_B[1]
    inRoomB = num_A_B[2]
    cost = 0

    sortedData = sorted(data,key=lambda x:abs(x[2]-x[1]), reverse=True)

    for team in sortedData:
        #B를 이용하는 것이 더 최소 비용일 경우
        if team[1]>team[2]:
            #B에 풍선이 충분히 남아있을 경우
            if team[0]<=inRoomB:
                inRoomB-=team[0]
                cost+=team[2]*team[0]
            #그렇지 않은 경우
            else:

                for _ in range(team[0]):
                    if inRoomB>0:
                        inRoomB-=1
                        cost+=team[2]
                    else:
                        inRoomA-=1
                        cost+=team[1]

        #A를 이용하는 것이 더 최소비용일 경우
        elif team[2]>team[1]:
            if team[0]<=inRoomA:
                inRoomA-=team[0]
                cost+=team[1]*team[0]
            else:
                
                for _ in range(team[0]):
                    if inRoomA>0:
                        inRoomA-=1
                        cost+=team[1]
                    else:
                        inRoomB-=1
                        cost+=team[2]

        #A,B까지의 거리가 같을 경우
        else:
            #아직 풍선이 더 많은 곳에서 뺄것
            if inRoomA<=inRoomB:
                inRoomB-=team[0]
                cost+=team[2]*team[0]
            else:
                inRoomA-=team[0]
                cost+=team[1]*team[0]                

    return cost

if __name__ == '__main__':
    input = sys.stdin.readline
    #[팀 수, A갯수, B갯수]
    while True:
    
        numTeams_A_B = list(map(int, sys.stdin.readline().split()))
        if sum(numTeams_A_B)==0:
            break
        
        data = []
        for i in range(0,numTeams_A_B[0]):
            #[풍선수, A거리, B거리] - [10,1,3][10,100,101]
            temp = list(map(int, sys.stdin.readline().split()))
            data.append(temp)

        res = solution(numTeams_A_B, data)

        print(res)