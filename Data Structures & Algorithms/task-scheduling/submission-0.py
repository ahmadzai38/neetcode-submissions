class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-i for i in count.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time +=1
            if heap:
                freq = heapq.heappop(heap)
                freq +=1
                if freq != 0:
                    q.append([freq,time+n])
            if q and q[0][1]== time:
                freq,readytime = q.popleft()
                heapq.heappush(heap,freq)
        return time
