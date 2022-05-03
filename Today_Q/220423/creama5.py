import collections



def longestStrChain(words):

    words.sort(key=len)
    dp = collections.defaultdict(int)
    for w in words:
        for i in range(len(w)):
            dp[w] = max(dp[w], dp[w[:i]+w[i+1:]]+1)
    return max(dp.values())


if __name__ == '__main__':
    n = ["bda", "bdca", "b", "ba", "bca"]

    n = longestStrChain(n)

    print(n)