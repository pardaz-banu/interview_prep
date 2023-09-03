#This is a leetcode Hard problem
#Fist Missing Positive Number
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st = set(nums)
        i = 1
        while i in st:
            i += 1
        return i
#another approach we can do using Hashing
