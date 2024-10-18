# nums = [2, 7, 11, 15]
# target = 9
# nums = [3,2,4] 
# target = 6
# nums = [3,3] 
# target = 6
nums = [3,2,3]
target = 6
position = []

length = len(nums)
for i in range(0, length):
    if (nums[i] + nums[i + 1]) == target:
        position.append(i)
        position.append(i + 1)
        break
    else:
        continue

print(position)


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        found = {}

        length = len(nums)
        for i in range(0, length):
            remainder = target - nums[i]

            if remainder in found:
                return [i, found[remainder]]
            else:
                found[nums[i]] = i
        

