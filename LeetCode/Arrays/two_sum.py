class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {x:nums.index(x) for x in nums}
        print(dict1)
        for i in range(len(nums)):
            if target-nums[i] in dict1.keys() and dict1[target-nums[i]]!=i:
                return [i,dict1[target-nums[i]]]
