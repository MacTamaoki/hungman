class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            print("for文" + i)
            for n in range(len(nums) - i):
                if nums[i] + nums[n] == target:
                    print(nums[i])

number = [1, 2, 6, 3, 5]
target = 4
go = Solution()
go.twoSum(number, target)