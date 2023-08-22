from math import factorial
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(factorial(len(nums))):
            p = len(nums) - 1
            while nums[p-1] > nums[p] and p > 0:
                p -= 1
            nums[p:] = reversed(nums[p:])
            if p > 0:
                q=p
                while nums[p-1]>nums[q]:
                    q += 1
                nums[p-1],nums[q] = nums[q],nums[p-1]
            #print(nums)
            res.append(copy.deepcopy(nums))
            
        #print(res)
        return res
