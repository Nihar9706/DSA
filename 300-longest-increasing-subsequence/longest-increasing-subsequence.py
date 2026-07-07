class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        ls=[1]*n
        ans=1 # max(ls)

        for i in range(n):
            for left in range(i):
                if nums[left]<nums[i]:
                    if ls[left]+1>ls[i]:
                        ls[i]=ls[left]+1
            ans=max(ans,ls[i])
        return ans