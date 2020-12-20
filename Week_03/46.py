class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [list(nums)]
        ret = []
        for num in nums:
            new_nums = set(nums)
            new_nums.remove(num)
            for item in self.permute(new_nums):
                ret.append([num] + item)
        return ret
