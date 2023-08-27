//IDEA - Take & Not Take

#include<bits/stdc++.h>
using namespace std;

void printVector(vector<int> nums)
{
    cout<<"\nVector: ";
    for(int i=0;i<nums.size();i++)
        cout<<nums[i]<<" ";
}

void subsequence(int index, vector<int> sub, vector<int> nums)
{
    if(index == nums.size())
    {
        printVector(sub);
        return;
    }
        
    //take
    sub.push_back(nums[index]);
    subsequence(index+1, sub, nums);
    
    //notTake
    sub.pop_back();
    subsequence(index+1, sub, nums);
}

int main()
{
    vector<int> nums = {3,1,2};
    subsequence(0,{},nums);
    return 0;
}
