class Solution {
public:

    int maximum(int a, int b)
    {
        if(a>b)
            return a;
        return b;
    }
    bool canJump(vector<int>& nums) 
    {
        if(nums[0] == 0)
        {
            if(nums.size() == 1)
                return true;
            return false;
        }

        int reachable = 0;
        for(int i=0;i<nums.size()-1;i++)
        {
            int curr = nums[i];
            if(curr == 0)
            {
                if(reachable > i)
                    continue;
                return false;
            }
            reachable = maximum(reachable,curr+i);
        }    
        if(reachable >= nums.size()-1)
            return true;
        return false;
    }
};
