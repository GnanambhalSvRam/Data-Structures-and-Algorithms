class Solution {
public:
    int maximum(int a, int b)
    {
        if(a>b)
            return a;
        return b;
    }

    int findMaxConsecutiveOnes(vector<int>& nums) 
    {
        int max = 0, count = 0, itr = 0;
        bool counting = false;

        while(itr<nums.size())
        {
            if(nums[itr] == 1)
            {
                if(counting)
                    count++;
                else
                {
                    counting = true;
                    max = maximum(max,count);
                    count = 1;
                }
            }
            else
                counting = false;

            ++itr;
        }

        return maximum(max,count);
    }
};
