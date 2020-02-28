class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev_element = self.countAndSay(n - 1)
            count = 0
            last_char = ""
            result = []
            for char in prev_element:
                if last_char != char:
                    if count:
                        result.append(count)
                        result.append(last_char)
                    count = 0
                last_char = char
                count += 1
            if len(result) and result[-1] == last_char:
                result[-2] += 1
            else:
                result.append(count)
                result.append(last_char)
            return "".join([str(i) for i in result])


if __name__ == '__main__':
    r = Solution().countAndSay(5)
    print(r)
