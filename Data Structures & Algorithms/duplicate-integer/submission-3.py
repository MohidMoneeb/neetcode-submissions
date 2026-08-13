class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        s = set()

        for i in range(len(nums)):
            if s.__contains__(nums[i]):
                return True
            else:
                s.add(nums[i])

        return False


        
        