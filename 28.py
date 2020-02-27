class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        dp = self.kmp(needle)
        state = 0
        matched_state = len(needle)
        for index, char in enumerate(haystack):
            state = dp[state][ord(char)]
            if state == matched_state:
                return index - state + 1
        return -1

    def kmp(self, pattern: str):
        pattern_length = len(pattern)
        dp = [[0 for _ in range(256)] for _ in range(pattern_length)]
        dp[0][ord(pattern[0])] = 1
        same_prefix_state = 0
        for state in range(1, pattern_length):
            for i in range(256):
                dp[state][i] = dp[same_prefix_state][i]
            dp[state][ord(pattern[state])] = state + 1
            same_prefix_state = dp[same_prefix_state][ord(pattern[state])]
        return dp


if __name__ == "__main__":
    s = Solution().strStr("aabba", "bba")
    print(s)