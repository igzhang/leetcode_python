class Solution:
    def romanToInt(self, s: str) -> int:
        roman_char_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        pre = roman_char_dict[s[0]]
        for i in range(1, len(s)):
            now = roman_char_dict[s[i]]
            if now > pre:
                total -= pre
            else:
                total += pre
            pre = now
        total += pre
        return total


if __name__ == '__main__':
    s = Solution().romanToInt("IV")
    print(s)
