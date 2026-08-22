class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        Hashmap = {}

        for i in range(len(nums)):
            Hashmap[nums[i]] = i

        for i in range(len(nums)):

            difference = target - nums[i]
            if difference in Hashmap and Hashmap[difference] != i:
                return [i, Hashmap[difference]]



            

