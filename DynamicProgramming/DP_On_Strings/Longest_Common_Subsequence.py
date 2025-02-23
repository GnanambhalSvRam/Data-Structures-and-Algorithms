class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        #This prints the longest common subsequence
        i,j = len(text1),len(text2)
        stack = []
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                stack.append(text1[i-1])
                i,j = i-1,j-1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i = i-1
                else:
                    j = j-1
        result = "".join(stack[::-1])
        print("The LCS is " + result)

        return dp[len(text1)][len(text2)]
