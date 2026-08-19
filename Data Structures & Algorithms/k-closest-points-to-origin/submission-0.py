class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = []
        for i,j in points:
            dist = i*i +j*j
            store.append([dist,i,j])
        heapq.heapify(store)
        res = []
        while k>0:
            d,i,j = heapq.heappop(store)
            res.append([i,j])
            k -=1
        return res