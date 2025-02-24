class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        hills, valleys = 0,0
        for i in range(1,len(nums)):
            ptrL, ptrR = i,i
            while ptrR < len(nums)-1 and nums[ptrL] == nums[ptrR+1]:
                ptrR += 1

            if ptrR == len(nums) - 1:
                break
            
            if nums[ptrL] < nums[ptrL-1] and nums[ptrR] < nums[ptrR+1]:
                valleys += 1

            if nums[ptrL] > nums[ptrL-1] and nums[ptrR] > nums[ptrR+1]:
                hills += 1

        return hills + valleys
