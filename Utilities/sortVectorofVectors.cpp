#include<bits/stdc++.h>
using namespace std;

bool sortFunc (const vector<int>& p1, const vector<int>& p2 ) 
{
    return p1[0] < p2[0];
}

void sortVector(vector<vector<int>> vec)
{
    sort(vec.begin(), vec.end(), sortFunc);
    
    for(int i=0;i<vec.size();i++)
    {
        for(int j=0;j<vec[i].size();j++)
            cout<<vec[i][j]<<" ";
        cout<<endl;
    }
    
    return;
}

int main()
{
    vector<vector<int>> vec = {{15,18},{2,6},{8,10},{1,3}};
    sortVector(vec);
    
    return 0;
}
