class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i]:
                # nums[zero], nums[i] = nums[i], nums[zero]
                nums[zero] = nums[i]
                if i != zero:
                    nums[i] = 0
                zero += 1
        return nums
