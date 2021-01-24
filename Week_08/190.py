class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            temp = (n & 1) << i
            ans += temp
            n >>= 1
        return ans
