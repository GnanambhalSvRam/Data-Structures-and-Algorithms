//Merge Array Intervals

#include<bits/stdc++.h>
using namespace std;

// void sort(&vector<vector<int>> intervals)
// {
    
// }

vector<vector<int>> mergeIntervals(vector<vector<int>> intervals)
{
    //sort(intervals);
    int start = intervals[0][0], end = intervals[0][1];
    vector<vector<int>> result;
    
    for(int i=1;i<intervals.size();i++)
    {
        if(intervals[i][0] > end)
        {
            vector<int> pair = {start,end};
            result.push_back(pair);
            cout<<"\nPushing back ["<<start<<","<<end<<"]";
            start = intervals[i][0];
            end = intervals[i][1];
            cout<<"\nCurrent start = "<<start<<", end = "<<end;
            continue;
        }
        
        if(intervals[i][0] <= end && intervals[i][1] > end)
            end = intervals[i][1];
    }
    
    result.push_back({start,end});
    
    for(int i=0;i<result.size();i++)
    {
        cout<<"\n\n"<<result[i][0]<<","<<result[i][1];
    }
    return result;
}

int main()
{
    vector<vector<int>> intervals = {{1,3},{2,6},{8,10},{15,18}}, res;
    res = mergeIntervals(intervals);
    
    cout<<"[ ";
    for(int i=0;i<intervals.size();i++)
        cout<<"["<<res[i][0]<<","<<res[i][1]<<"] ";
    cout<<"]";
    
    return 0;
}
