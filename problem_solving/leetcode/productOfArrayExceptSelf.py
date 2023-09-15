class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        p = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                p *= nums[i]
        for i in range(len(nums)):
            if count == 1:
                if nums[i] == 0:
                    res.append(p)
                else:
                    res.append(0)
            elif count > 1:
                res.append(0)
            else:
                res.append(p//nums[i])
        return res
