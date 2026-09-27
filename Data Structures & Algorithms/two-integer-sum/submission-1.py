class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            deff = target - nums[i]
            if deff in hashset:
                return [hashset[deff],i]
            hashset[nums[i]] = i 