"""
The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

"""


def hindex(citations):
    citations.sort(reverse=True)
    h = 0
    for i, cite in enumerate(citations):
        if i < cite:
            h += 1
        else:
            break
    return h

# Example usage:
print(hindex([7, 8, 9, 1, 4, 4, 5, 5]))
