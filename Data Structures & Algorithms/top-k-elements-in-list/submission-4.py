class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #BUCKET SORT
        count={}
        freq= [[] for i in range(len(nums)+1)] #1 because to count from 1 because at min, 1 unique number will be there as a count of elements
        #nums = [1, 1, 1, 2, 2, 100], count becomes {1: 3, 2: 2, 100: 1}.(for above)
        for n in nums:
            count[n]= 1+ count.get(n,0)
        for n,c in count.items(): #.items return key value pair in dictionary
            freq[c].append(n)
        res=[]

        for i in range(len(freq)-1,0,-1): #going decremented way
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res







    



        