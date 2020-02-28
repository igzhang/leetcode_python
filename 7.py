class Solution:
    def reverse(self, x: int) -> int:
        total = 0
        int_max = 2 ** 31 - 1
        x1 = abs(x)
        while x1 != 0:
            pop = x1 % 10
            x1 = x1 // 10
            if (total > (int_max / 10)) or ((total == (int_max/10)) and (pop > 7)):
                return 0
            total = total * 10 + pop
        if x > 0:
            return total
        else:
            return -total


if __name__ == '__main__':
    s = Solution().reverse(1534236469)
    print(s)
