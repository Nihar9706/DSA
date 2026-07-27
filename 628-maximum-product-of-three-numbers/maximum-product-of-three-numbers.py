class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1=max2=max3=0
        min1=min2=0
        nums.sort()
        return max((nums[-1]*nums[-2]*nums[-3]),(nums[0]*nums[1]*nums[-1]))




        