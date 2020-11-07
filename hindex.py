"""
The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

"""


def hindex(lis=[ 7, 8, 9, 1 ]):
    if len(lis) == 0:
        return 0
    for j in range(max(lis), -1, -1):
        check = [ x - j for x in lis ]
        PosCount = len(list(filter(lambda x: (x >= 0), check)))
        if j <= PosCount:
            return j


print(hindex())
