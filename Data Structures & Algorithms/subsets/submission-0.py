class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets,curset=[],[]
        self.helper(0,nums,curset,subsets)
        return subsets


    def helper(self, i,nums,currSet,subsets):
        if i>=len(nums):
            subsets.append(currSet.copy())
            return

        
        currSet.append(nums[i])
        self.helper(i+1,nums,currSet,subsets)
        currSet.pop()

        self.helper(i+1,nums,currSet,subsets)


        
        