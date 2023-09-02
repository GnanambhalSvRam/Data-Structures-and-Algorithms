class Solution {
public:
    bool canJump(vector<int>& nums) 
    {
        int post = nums.size()-1;
        bool flag = true;

        while(post > 0)
        {
            cout<<"\nCurrently at location "<<post;
            int itr, i, count;
            itr = i = post-1;
            count = 1;

            for(;i>=0;i--)
            {
                if(nums[i] >= count)
                    break;
                count++;
            }

            if(i>=0)
            {
                cout<<"\nNow moving the post to "<<i;
                post = i;
            }
            else
            {
                flag = false;
                cout<<"\nThe current value of i is "<<i;
                cout<<"\nBreaking out of the loop!\n\n";
                break;
            }
        }

        return flag;    
    }
};
