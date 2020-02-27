from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for index in range(1, len(strs)):
            current_element = strs[index]
            k = 0
            max_length = min(len(prefix), len(current_element))
            while k < max_length and prefix[k] == current_element[k]:
                k += 1
            prefix = prefix[:k]
            if not prefix:
                return ""
        return prefix


if __name__ == "__main__":
    result = Solution().longestCommonPrefix(["dog","racecar","car"])
    print(result)
