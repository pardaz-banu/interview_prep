from copy import deepcopy
class Solution:
    res = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        def permute(temp, nums):
            if len(nums) == 0:
                res.append(temp)
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                permute(temp+[nums[i]], nums[:i]+nums[i+1:])
        nums.sort()
        permute([],nums)
        return res
                
        
        

