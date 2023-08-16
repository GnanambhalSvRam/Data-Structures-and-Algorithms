//LeetCode 1464. Maximum Product of Two Elements in an Array
class Solution {
public:
    int maxProduct(vector<int>& nums) 
    {
        if(nums.size()<=1)
            return -1;

        int first, second, n = nums.size(), loc = 0;
        first = nums[0];
        second = INT_MIN;
        for(int i=1;i<n;i++)
        {
            if(nums[i]>first)
            {
                second = first;
                first = nums[i];
                loc = i;
                continue;
            }
            
            if(nums[i]>second)
                second = nums[i];
        }
        if(second == INT_MIN)
            second = first;
        
        cout<<"\nLargest = "<<first<<"\nSecond Largest = "<<second;

        return (first-1)*(second-1);
    }
};
