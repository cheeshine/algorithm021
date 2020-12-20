class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n + 1)]

        if n == k:
            return [list(range(1, n + 1))]

        part1 = self.combine(n - 1, k)
        part2 = self.combine(n - 1, k - 1)
        [item.append(n) for item in part2]
        return part1 + part2
