#include<bits/stdc++.h>
using namespace std;

void printVector(vector<int> nums)
{
    cout<<"\nVector: ";
    for(int i=0;i<nums.size();i++)
        cout<<nums[i]<<" ";
}

void subsequence(int index, int sum, vector<int> sub, vector<int> nums, int k)
{
    //base cases
    if(index == nums.size())
    {
        if(sum == k)
            printVector(sub);
        return;
    }
    if(sum == k && index == nums.size())
    {
        printVector(sub);
        return;
    }
    
    //recursive cases
    sub.push_back(nums[index]);
    subsequence(index+1,sum+nums[index],sub,nums,k);
    
    sub.pop_back();
    subsequence(index+1,sum,sub,nums,k);
}

int main()
{
    vector<int> nums = {1,2,1,0};
    subsequence(0,0,{},nums,2);
    return 0;
}
