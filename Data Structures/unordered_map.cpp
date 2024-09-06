#include<bits/stdc++.h>
using namespace std;

int main()
{
    unordered_map<int,string> attendance = {
        {1, "Joey Tribianni"},
        {2, "Rachel Green"},
        {3, "Phoebe Buffay"},
        {4, "Monica Geller"}
    };
    
    attendance[5] = "Chandler Bing";
    
    for(auto student : attendance)
    {
        cout<<"\n"<<student.first<<" : "<<student.second;
    }
    
    for(auto itr = attendance.begin(); itr!=attendance.end(); itr++)
    {
        cout<<"\n"<<itr->first<<": "<<itr->second;
    }
    
    int key = 7;
    if(attendance.find(key) != attendance.end())
        cout<<"\nKey found in the hashmap";
    else
        cout<<"\nKey is not found in the hashmap!";
        
    cout<<"\nThe size of the hashmap is: "<<attendance.size();
    
    return 0;
}
