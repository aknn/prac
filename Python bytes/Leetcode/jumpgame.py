"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

"""


class Solution:
    def Jump(self, nums) -> int:
        if not nums or len(nums) == 1:
            return True
        des = len(nums) - 1
        for I in range(des - 1, -1, -1):
            if I + nums[ I ] >= des:
                des = I
            if des == 0:
                return True


obj = Solution()
print(obj.Jump([ 2, 3, 0, 1, 4 ]))
