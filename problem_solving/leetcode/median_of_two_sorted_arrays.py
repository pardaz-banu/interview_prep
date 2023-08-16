class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        if len(merge)%2 == 1:
            return merge[len(merge)//2]
        else:
            #print(merge[(len(merge)//2)-1])
            #print(merge[(len(merge)//2)])
            return (merge[(len(merge)//2)-1] + merge[(len(merge)//2)])/2
