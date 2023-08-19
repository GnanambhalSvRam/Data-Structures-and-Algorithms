#include<bits/stdc++.h>
using namespace std;

bool validParantheses(string s)
{
    stack<char> stk;
    for(int i=0;i<s.size();i++)
    {
        char ch = s[i];
        if(ch == '(' || ch == '{' || ch == '[')
            stk.push(ch);
        
        else if(!stk.empty && (ch == ')' && stk.top() == '(' || ch == '}' && stk.top() == '{' || ch == ']' && stk.top() == '['))
            stk.pop();
            
        else
            return false;
    }
    
    if(stk.empty())
        return true;
    return false;
}

int main()
{
    string s = "{}()[[]";
    bool res = validParantheses(s);
    cout<<"\nAnswer = "<<res;
    
    return 0;
}
