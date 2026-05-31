class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        long = 0
        for n in nums:
            if n-1 not in num_set:
                length =0
                while(n + length) in num_set:
                    length += 1
                long = max(long,length)
        return long
