'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string '''


def longestCommonPrefix(strs):
    def compare2(a, b):
        lcp = ''
        if not a or not b:
            return ""
        length = min(len(a), len(b))
        for i in range(0, length):
            if a[ i ] == b[ i ]:
                lcp += a[ i ]
            else:
                break
        return lcp

    prefix = compare2(strs[ 0 ], strs[ 1 ])
    for j in range(2, len(strs)):
        prefix = compare2(prefix, strs[ j ])
    return prefix
