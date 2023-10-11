'''Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
'''

class Solution(object):
    def sortArray(self, nums):
        if len(nums) > 1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            self.sortArray(left)
            self.sortArray(right)
            i,j,k=0,0,0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                nums[k] = left[i]
                i+= 1
                k += 1
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            return nums
        else:
            return nums


        
