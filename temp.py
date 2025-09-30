class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

new = Solution()
L = [1, 4, 3, 5, 6, 22, 13,34,12,41,9]
output = new.twoSum(L, 56)
print(output)