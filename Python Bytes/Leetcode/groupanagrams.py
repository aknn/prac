"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,

typically using all the original letters exactly once.



"""
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map, result = collections.defaultdict(list), [ ]
        for s in strs:
            sorted_str = ("").join(sorted(s))
            anagrams_map[ sorted_str ].append(s)

        for anagram in anagrams_map.values():
            anagram.sort()
            result.append(anagram)

        return result


if __name__ == "__main__":
    result = Solution().groupAnagrams([ "eat", "tea", "tan", "ate", "nat", "bat" ])
    print(result)
