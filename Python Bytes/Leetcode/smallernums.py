""" How Many Numbers Are Smaller Than the Current Number


Given the array nums, for each nums[i] find out how many numbers
 in the array are smaller than it. That is, for each nums[i] you
  have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array."""


def smallerNumbersThanCurrent(nums):
    # [8,3,2,2,1]

    sorted_num = sorted(nums, reverse=True)
    dacount = { }
    for i in range(len(sorted_num) - 1):
        if sorted_num[ i ] > sorted_num[ i + 1 ]:
            dacount[ sorted_num[ i ] ] = len(sorted_num) - (i + 1)
    dacount[ sorted_num[ -1 ] ] = 0

    output = [ ]
    for num in nums:
        output.append(dacount[ num ])

    return output


print(smallerNumbersThanCurrent([ 8, 4, 5, 3, 3, 2, 2, 2, 1 ]))
