#include<bits/stdc++.h>
using namespace std;

int findMax(int a, int b)
{
    if(a>b)
        return a;
    return b;
}

int largestSubStr(string s)
{
    map<char,int> table;
    int len = 0, start = 0, end = 0, max = 1;
    for(int i=0;i<s.length();i++)
    {
        cout<<"\nCharacter: "<<s[i];
        if(table.find(s[i]) == table.end())
        {
            cout<<"\n"<<s[i]<<" NOT IN table";
            table[s[i]] = i;
            len++;
            cout<<"\nCurrent length = "<<len<<endl;
        }
        else
        {
            cout<<"\n"<<s[i]<<" IN table";
            start = table[s[i]] + 1;
            max = findMax(len,max);
            len = i-start+1;
            cout<<"\nCurrent length = "<<len<<endl;
        }
    }
    
    return findMax(max,len);
}

int main()
{
    string s = "substring";
    int res = largestSubStr(s);
    cout<<"\nResult = "<<res;
    return 0;
}
