#include<bits/stdc++.h>
using namespace std;

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
