#include<bits/stdc++.h>
#include<cstdlib>
using namespace std;

int max(int a, int b)
{
    if(a>b)
        return a;
    return b;
}

int maxSum(int arr[], int n)
{
    if(n==0) return 0;
    if(n==1) return arr[0];
    
    int res[n];
    res[0] = arr[0];
    res[1] = max(arr[0], arr[1]);
    
    for(int i=2; i<n; i++)
        res[i] = max(res[i-1], res[i-2]+arr[i]);
        
//     cout<<"\nPrinting res array: ";
//     for(int i=0;i<n;i++)
//         cout<<res[i]<<" ";
        
    return res[n-1];
}

int main()
{
    int arr[] = {4,1,6,3,2}, n=5;
    int result = maxSum(arr,n);
    cout<<"\nThe Maximum Sum of Non-Adjacent Elements is "<<result;
    
    return 0;
}
