from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plusPart(digits, len(digits)-1)

    def plusPart(self, digits: List[int], right: int):
        if digits[right] < 9:
            digits[right] += 1
            return digits
        digits[right] = 0
        if right == 0:
            return [1 if i == 0 else 0 for i in range(len(digits)+1)]
        return self.plusPart(digits, right-1)


if __name__ == "__main__":
    res = Solution().plusOne([0])
    print(res)
