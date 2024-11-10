"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,

typically using all the original letters exactly once.



"""
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = collections.defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)
            anagrams_map[key].append(s)
        return [sorted(group) for group in anagrams_map.values()]


if __name__ == "__main__":
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
