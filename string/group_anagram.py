import collections


def groupAnagrams(strs):
    anagrams = collections.defaultdict(list) # 키값을 정해주는 배열이다.

    print('defaultdict : ' + str(anagrams.default_factory))

    for word in strs:

        print("origin : " + word + ", sorted : " + str(sorted(word)))
        print("''.join(sorted(word))'' : " + ''.join(sorted(word)))
        # list 벗기기 위해 .join 이용
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


if __name__ == '__main__':

    n = ["eat" , "tea" , "tan" , "ate" , "nat" , "bat"]

    n = groupAnagrams(n)

    print(n)