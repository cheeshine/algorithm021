class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_num = ten_num = 0
        for bill in bills:
            if bill == 5:
                five_num += 1
            elif bill == 10 and five_num:
                ten_num += 1
                five_num -= 1
            elif bill == 20 and ten_num and five_num:
                    ten_num -= 1
                    five_num -= 1
            elif bill == 20 and five_num >= 3:
                    five_num -= 3
            else:
                break
        else:
            return True
        return False
