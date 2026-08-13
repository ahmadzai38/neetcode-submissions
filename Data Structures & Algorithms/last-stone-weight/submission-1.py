class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = []
        for i in stones:
            new_stones.append(-i)
        heapq.heapify(new_stones)
        while len(new_stones)>1:
            f = heapq.heappop(new_stones)
            s = heapq.heappop(new_stones)
            if s>f:
                cur = f - s
                heapq.heappush(new_stones,cur)
        return abs(new_stones[0]) if new_stones else 0

