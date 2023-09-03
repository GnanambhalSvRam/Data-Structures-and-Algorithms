class Solution {
public:
    int maximum(int a, int b)
    {
        if(a>b)
            return a;
        return b;
    }

    int jump(vector<int>& nums) 
    {
        int res = 0, left = 0, right = 0;
        while(right < nums.size()-1)
        {
            int farthest = 0;
            for(int i=left;i<=right;i++)
                farthest = maximum(farthest, i + nums[i]);
            
            left = right + 1;
            right = farthest;
            res++;
        }

        return res;
    }
};
