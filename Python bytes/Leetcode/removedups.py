


"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


def removeDuplicates(nums=[1,2,3,3,3,4,4,4]):
        if len(nums)==0:
            return 0
        j=0
        for i in range(len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]

        return j+1
#driver code
if __name__=="__main__":
    print(removeDuplicates())