class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        Hash = set()

        for i in range(len(nums)):
            if nums[i] in Hash:
                return True
            Hash.add(nums[i])

        return False
            

        