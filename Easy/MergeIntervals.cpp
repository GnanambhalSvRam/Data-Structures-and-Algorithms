//Merge Array Intervals
//Time Complexity: O(nlogn)
#include<bits/stdc++.h>
using namespace std;

static bool sortFunc(const vector<int> &p1, const vector<int> &p2)
{
    return p1[0] < p2[0];
}

vector<vector<int>> merge(vector<vector<int>>& intervals) 
{
    sort(intervals.begin(), intervals.end(), sortFunc);
    int start = intervals[0][0], end = intervals[0][1];

    vector<vector<int>> res;
    vector<int> pair;

    for(int i=1;i<intervals.size();i++)
    {
        if(intervals[i][0] <= end)
        {
                if(intervals[i][1] < end)
                    continue;
                else
                    end = intervals[i][1];
        }
            
        else
        {
                res.push_back({start,end});
                start = intervals[i][0];
                end = intervals[i][1];
        }
    }
        
    res.push_back({start,end});

    return res;
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
