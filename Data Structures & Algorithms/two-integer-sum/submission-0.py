class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,n in enumerate(nums):
            deff = target - n
            if deff in hash:
                return [hash[deff],i]
            hash[n] = i