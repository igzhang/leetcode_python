class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or ((x % 10 == 0) and (x != 0)):
            return False
        total = 0
        while x > total:
            pop = x % 10
            x = x // 10
            total = total * 10 + pop
        return x == total or x == (total // 10)


if __name__ == '__main__':
    s = Solution().isPalindrome(101)
    print(s)
