class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        
        seen_pairs = set()
        for i in range(len(unique_nums)):
            for j in range(i, len(unique_nums)):
                seen_pairs.add(unique_nums[i] ^ unique_nums[j])
                
        unique_triplets = set()
        for p in seen_pairs:
            for num in unique_nums:
                unique_triplets.add(p ^ num)
                
        return len(unique_triplets)