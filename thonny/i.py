class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        g=sorted(nums1+nums2)
        d=f=0
        for i in range(0,len(g)):
            d+=g[i]
        if d==0:
            return d
        else:
            f=float(d/(len(g)))
            return f
nums1=[1,2]
nums2=[3,4]
r1=Solution()
print(r1.findMedianSortedArrays(nums1,nums2))

# class Solution(object):
#     def maxProduct(self, nums):
#         g=sorted(nums)
#         j=g[len(g)-1]
#         i=h=g[len(g)-2]
#         for _ in range(j):
#             i+=h
#         return h
# nums=[3,4,5,2]
# r1=Solution()
# print(r1.maxProduct(nums))