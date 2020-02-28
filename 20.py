class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length % 2 == 1:
            return False
        mapping_dict = {")": "(", "}": "{", "]": "["}
        stack = []
        stack_length = 0
        for char in s:
            if char in mapping_dict:
                last_element = stack.pop() if stack_length > 0 else "#"
                if last_element != mapping_dict[char]:
                    return False
                stack_length -= 1
            else:
                stack.append(char)
                stack_length += 1
                if stack_length > (length / 2):
                    return False
        return stack_length == 0


if __name__ == '__main__':
    result = Solution().isValid("{[]}")
    print(result)