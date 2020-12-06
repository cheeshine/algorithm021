class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p_nums1_now = m - 1
        p_empty = m + n -1
        p_nums2_now = n - 1
        while p_nums2_now >= 0:
            if nums2[p_nums2_now] >= nums1[p_nums1_now]:
                nums1[p_empty] = nums2[p_nums2_now]
                p_empty -= 1
                p_nums2_now -= 1
            else:
                nums1[p_empty] = nums1[p_nums1_now]
                p_nums1_now -= 1
                p_empty -= 1
            if p_nums1_now < 0:
                for i in range(p_nums2_now + 1):
                    nums1[i] = nums2[i]
                p_nums2_now = -1

        return nums1