class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_nums = {}
        search_nums[nums[0]] = 0
        for j in range(1, len(nums)):
            num_b = nums[j]
            num_a = target - num_b
            if num_a in search_nums:
                for i in range(len(search_nums)):
                    if nums[i] == num_a:
                        return [i, j]
            else:
                search_nums[num_b] = j
