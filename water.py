"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

"""


def Maxarea(bars):
    l = 0
    r = len(bars) - 1
    area = 0

    while l < r:
        area = max(area, min(bars[ l ], bars[ r ]) * (r - l))

        if bars[ l ] < bars[ r ]:
            l += 1
        else:
            r -= 1
    return area


# Driver code
x = [ 1, 2, 4, 3, 8, 5 ]

print(Maxarea(x))
