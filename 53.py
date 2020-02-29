from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_length = len(nums)
        max_value = nums[0]
        if nums_length == 1:
            return max_value
        for i in range(1, nums_length):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_value = max(nums[i], max_value)
        return max_value


if __name__ == "__main__":
    s = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(s)
