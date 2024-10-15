class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        def binarySearch(self, nums: List[int], target: int, hi: int, lo: int):

            if hi < lo:
                return hi+1

            mid = (hi+lo)//2

            if target == nums[mid]:
                return mid

            if hi == lo:
                if target > nums[hi]:
                    return hi+1
                else:
                    return hi
            
            if target > nums[mid]:
                return binarySearch(self, nums, target, hi, mid+1)
            
            else:
                return binarySearch(self, nums, target, mid-1, lo)

        return binarySearch(self, nums, target, len(nums)-1, 0)
