class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset[nums[i]]=0
            hashset[nums[i]] +=1
        sorted_keys = sorted(hashset,key=hashset.get,reverse = True)
        return sorted_keys[:k]
