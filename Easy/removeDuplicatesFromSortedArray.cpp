#include<bits/stdc++.h>
using namespace std;

void printVector(vector<int> nums)
{
    cout<<"\nPrinting vector: ";
    for(int i=0; i<nums.size();i++)
        cout<<nums[i]<<" ";
}

int removeDuplicate(vector<int>& nums) 
{
    int comp = nums[0], index = 1;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i] == comp)
                continue;
                
            nums[index] = comp = nums[i];
            index++;
        }
        return index;
}

int main()
{
    vector<int> nums = {1,2};
    int res = removeDuplicate(nums);
    cout<<"\nAnswer = "<<res;
    
    return 0;
}
