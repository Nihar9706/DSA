class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                arr.append(i)
        return arr
