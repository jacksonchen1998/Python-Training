class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            j = target - i # Find the first number in array
            strat_index = nums.index(i)
            next_index = strat_index + 1
            temp_nums = nums[next_index:] # Use the last array for searching second number
            if j in temp_nums:
                return (strat_index, next_index + temp_nums.index(j))

    def twoSum_d(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i # Store index for the number
            else:
                return [dict[target - nums[i]], i]


nums = [2, 4, 6, -1]
s = Solution()
print(s.twoSum(nums, 9))
print(s.twoSum_d(nums, 9))