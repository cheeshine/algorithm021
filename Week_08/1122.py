class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = max(arr1)
        cnt = [0] * (count + 1)
        res = []
        for num in arr1:
            cnt[num] += 1

        for num in arr2:
            res.extend([num] * cnt[num])
            cnt[num] = 0

        for i in range(1, count + 1):
            if cnt[i]:
                res.extend([i] * cnt[i])
        return res
