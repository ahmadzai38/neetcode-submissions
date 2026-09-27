class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = {}
        for s in strs:
            sig = "".join(sorted(s))
            if sig not in hashset:
                hashset[sig]= []
            hashset[sig].append(s)
        return list(hashset.values())

