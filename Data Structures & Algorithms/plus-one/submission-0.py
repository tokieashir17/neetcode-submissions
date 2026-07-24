class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)
        for n in range(i - 1, -1, -1): 
            if digits[n] < 9 :
                digits[n] += 1
                return digits
            digits[n] = 0

        return [1] + digits

