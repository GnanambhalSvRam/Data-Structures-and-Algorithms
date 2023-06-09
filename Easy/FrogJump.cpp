#include<bits/stdc++.h>
#include<cstdlib>
using namespace std;

int min(int a, int b)
{
    if(a<b)
        return a;
    return b;
}

int frogJump(int n, vector<int> height)
{
    if(n == 0 || n == 1)
        return n;
    
    vector<int> energy(n,0);
    energy[0] = 0;  //stair 1
    energy[1] = abs(height[0]-height[1]); //stair 2
    
    for(int i=2;i<n;i++)
        energy[i] = min((energy[i-1] + abs(height[i-1]-height[i])), (energy[i-2] + abs(height[i-2]-height[i])));
    
    return energy[n-1];
}

int main()
{
    int n = 4;
    vector<int> height = {10,20,30,10};
    int minEnergy = frogJump(n, height);
    cout<<"\nThe minimum energy required by the frog is : "<<minEnergy;
    return 0;
}
