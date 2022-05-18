import collections


def gr_ana(n):
    anagram = collections.defaultdict(list)
    
    for word in n:
        anagram[''.join(sorted(word))].append(word)
    return anagram.values()


if __name__ == '__main__':
    n = ["eat", "tea", "tan", "ate", "nat", "bat"]

    n = gr_ana(n)

    print(n)