"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

"""


def firstUniqChar(s: str) -> int:
    dict = { }
    for i in s:
        if i in dict:
            dict[ i ] += 1
        else:
            dict[ i ] = 1
    v = [ i for i in dict.keys() if dict[ i ] == 1 ]
    if len(v) == 0:
        return -1
    else:
        return s.find(v[ 0 ])
