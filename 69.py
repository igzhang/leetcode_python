class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 0
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = mid ** 2
            if sqrt == x:
                return mid
            elif sqrt > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    res = Solution().mySqrt(1)
    print(res)
