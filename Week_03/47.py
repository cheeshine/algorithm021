class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [list(nums)]
        ret = []
        for num in set(nums):
            new_nums = nums.copy()
            new_nums.remove(num)
            for item in self.permuteUnique(new_nums):
                ret.append([num] + item)
        return ret