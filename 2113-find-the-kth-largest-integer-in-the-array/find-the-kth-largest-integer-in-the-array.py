class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap=[-int(i)for i in (nums)]
        heapq.heapify(heap)
        while k>1:
            heapq.heappop(heap)
            k-=1
        return str(-heap[0])