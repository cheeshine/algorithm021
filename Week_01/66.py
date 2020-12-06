class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1, len(digits) + 1):
            if digits[-i] == 9:
                digits[-i] = 0
            else:
                digits[-i] += 1
                break
        else:
            digits[0] = 1
            digits.append(0)
        return digits
