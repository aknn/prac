"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



"""


def revstr(str=[ 'r', 'e', 'v', 'e', 'r', 's', 'e' ]):
    l, r, temp = 0, len(str) - 1, 0
    while l < r:
        str[ l ], str[ r ] = str[ r ], str[ l ]
        l += 1
        r -= 1
    return str


print(revstr())
