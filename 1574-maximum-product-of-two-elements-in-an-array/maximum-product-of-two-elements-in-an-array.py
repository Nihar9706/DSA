class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)>=2:
            max1=max(nums)
            nums.remove(max(nums))
            max2=max(nums)
            return (max1-1)*(max2-1)
        elif len(nums)==1:
            return nums[0]
        else:
            return 0