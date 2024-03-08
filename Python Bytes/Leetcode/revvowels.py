"""
Write a function that takes a string as input and reverse only the vowels of a string.

"""


def reverse_vowel(s):
    vowels = "AEIOUaeiou"
    i, j = 0, len(s) - 1
    s = list(s)

    while i < j:
        while i < j and s[ i ] not in vowels:
            i += 1
        while i < j and s[ j ] not in vowels:
            j -= 1

        s[ i ], s[ j ] = s[ j ], s[ i ]
        i, j = i + 1, j - 1
    return "".join(s)


print(reverse_vowel('adele'))
