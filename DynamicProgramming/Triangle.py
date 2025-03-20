class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        n = len(triangle[m-1])
        INF = float('inf')

        dp = [[INF for _ in range(n+1)] for _ in range(m+1)]

        dp[1][1] = triangle[0][0]

        minVal = INF
        for i in range(2,m+1):
            for j in range(1,len(triangle[i-1])+1):
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i-1][j-1]

        return min(dp[m])
