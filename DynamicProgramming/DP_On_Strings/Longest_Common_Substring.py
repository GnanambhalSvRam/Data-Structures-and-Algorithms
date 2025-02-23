#brute force approach
def lcs(str1: str, str2: str) -> int:
    
    maxCount = 0
    def recurse(idx1,idx2,count):
        nonlocal maxCount
        if idx1 >= len(str1) or idx2 >= len(str2):
            return

        if str1[idx1] == str2[idx2]:
            maxCount = max(maxCount, count+1)
            recurse(idx1+1, idx2+1, count+1)

        recurse(idx1+1,idx2,0)
        recurse(idx1,idx2+1,0)

        return

    recurse(0,0,0)
    return maxCount
  #Time complexity exceeded

#Bottom-Up Memoization Approach
def lcs(str1: str, str2: str) -> int:
    
    str1 = '#' + str1
    str2 = '#' + str2

    dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    maxVal = 0

    for i in range(1,len(str1)):
        for j in range(1,len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxVal = max(dp[i][j], maxVal)

            else:
                dp[i][j] = 0

    return maxVal

