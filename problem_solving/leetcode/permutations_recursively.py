from math import factorial
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res=[]
        def permuteOf(nums, st=0):
            if st == len(nums)-1:
                res.append(deepcopy(nums))
            else:
                for i in range(st, len(nums)):
                    nums[i],nums[st] = nums[st],nums[i]
                    permuteOf(nums, st+1)
                    nums[i],nums[st]=nums[st],nums[i]
        permuteOf(nums)
        return res
