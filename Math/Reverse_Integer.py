class Solution:
    def reverse(self, x: int) -> int:
        
        MAX, MIN = (2 ** 31) - 1, -1 * (2 ** 31) 
        queue = deque()
        neg = False
        if x < 0:
            neg = True
            x = -1 * x

        while x > 0:
            element = x%10
            queue.append(element)
            x = x // 10

        ans = 0
        while queue:
            ans = ans * 10 + queue.popleft()

        if neg:
            ans = -1 * ans

        if ans > MAX or ans < MIN:
            ans = 0

        return ans
