class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        INF, m, n = float('inf'), len(matrix), len(matrix[0])

        dp = [[INF for _ in range(n+2)] for _ in range(m)]

        for i in range(m):
            dp[i][0] = dp[i][n+1] = INF

        for j in range(1,n+1):
            dp[0][j] = matrix[0][j-1]

        for i in range(1,m):
            for j in range(1,n+1):
                dp[i][j] = matrix[i][j-1] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

        return min(dp[m-1])
