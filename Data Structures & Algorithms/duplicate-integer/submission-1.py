class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        HashSet = set()

        for i in range(len(nums)):
            if nums[i] in HashSet:
                return True
            HashSet.add(nums[i])

        return False