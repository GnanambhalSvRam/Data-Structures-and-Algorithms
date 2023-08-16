#include<bits/stdc++.h>
using namespace std;

bool solution(vector<int> vec)
{
    if(vec.size() <= 1)
        return true;
        
    for(int i=1;i<vec.size();i++)
    {
        if(vec[i]>vec[i-1] || vec[i]==vec[i+1])
            continue;
        else
            return false;
    }
    return true;
}

int main()
{
    vector<int> vec{3,4,6,5,10};
    bool res = solution(vec);
    cout<<"\nAnswer = "<<res;
    
    return 0;
}
