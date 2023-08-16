#include<bits/stdc++.h>
using namespace std;

//Single Traversal Approach
int secondLargestElementOptimized(vector<int> vec)
{
    int first, second, n = vec.size();
    first = vec[0];
    second = INT_MIN;
    
    for(int i=1;i<n;i++)
    {
        if(vec[i]>first)
        {
            second = first;
            first = vec[i];
            continue;
        }
        
        if(vec[i]>second && vec[i] != first)
            second = vec[i];
    }
    
    if(second == INT_MIN)
        return -1;
    return second;
}

//Dual Traversal Approach
int secondLargestElement(vector<int> vec)
{
    int max = vec[0];
    int ans = -1;
    
    //Loop 1
    for(int i=1;i<vec.size();i++)
        if(vec[i]>max)
            max = vec[i];
            
    //Loop 2
    int diff = INT_MAX;
    for(int i=0;i<vec.size();i++)
    {
        if(max != vec[i] && max-vec[i]<diff)
        {
            diff = max-vec[i];
            ans = vec[i];
        }    
    }
    
    return ans;
}

int main()
{
    int n = 3;
    int arr[n] = {2,2,2};
    vector<int> vec(arr,arr+n);
    int ans = secondLargestElement(vec);
    cout<<"\n"<<ans;
    return 0;
}
