import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)  # Step 1: Count frequencies in freq dictionary
        heap=[] # Min-heap to store (frequency, number)
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num)) # Min-heap sorts by frequency
            if(len(heap)>k):
                heapq.heappop(heap)
        return [num for _, num in heap]     

        #(O(n log k))   
        