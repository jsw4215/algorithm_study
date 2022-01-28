"""
티켓은 [출발, 도착] 으로 이루어짐
'JFK'에서 출발해야 한다
알파벳순서로 정렬
"""
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {start: [] for start, end in tickets}  # list 첫번째 요소: 키 / 빈 list: 값
        for start, end in sorted(tickets):
            dic[start].append(end)  # 키에 해당하는 값 넣어주기

        result = ["JFK"]  # 'JFK'에서 출발해야함

        def dfs(start):
            if len(result) == len(tickets) + 1:  # 결과의 전체길이 == 티켓길이+1(JFK)
                return True

            if start not in dic:  # (JFK)가 딕셔너리에 없으면
                return False

            temp = list(dic[start])  # 해당 키에 대한 밸류값

            for i, v in enumerate(temp):  # temp에 있는 값을 v, 인덱스를 i
                dic[start].pop(i)  # 딕셔너리에서 비교한 값 i번째 값을 빼줌
                result.append(v)  # 결과에 값을 넣어줌

                if dfs(v):  # 값이 존재하면 리턴 트루
                    return True
                dic[start].insert(i, v)  # 키에 대한 밸류가 없을때
                result.pop()
            return False

        dfs("JFK")
        return result

    print(findItinerary('', [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))