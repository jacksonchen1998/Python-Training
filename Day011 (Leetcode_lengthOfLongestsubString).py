# Leetcode Qusetion 3

class Solution(object):
    def lengthOfLongestsubString(self, s):
        start = -1
        max = 0
        dict = {}

        for i in range(len(s)):
            if s[i] in dict and start < dict[s[i]]:
                start = dict[s[i]]
                dict[s[i]] = i
            else:
                dict[s[i]] = i
                if max < i - start:
                    max = i - start
        
        return max

def main():
    sol = Solution()
    str_1 = "abcdefff"
    str_2 = " "
    str_3 = "acctdf"
    str_4 = "aaaa"
    str_empty = ""
    print("str_1: ", sol.lengthOfLongestsubString(str_1))
    print("str_2: ", sol.lengthOfLongestsubString(str_2))
    print("str_3: ", sol.lengthOfLongestsubString(str_3))
    print("str_4: ", sol.lengthOfLongestsubString(str_4))
    print("str_empty: ", sol.lengthOfLongestsubString(str_empty))

main()
