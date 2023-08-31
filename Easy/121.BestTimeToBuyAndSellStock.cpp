class Solution {
public:
    int maxProfit(vector<int>& stocks) 
    {
        int lsf = INT_MAX, pist, maxProfit = 0;
        for(int i=0;i<stocks.size();i++)
        {
            if(stocks[i] < lsf)
                lsf = stocks[i];
            //cout<<"\nlsf at iteration "<<i<<" = "<<lsf;

            pist = stocks[i] - lsf;

            if(pist > maxProfit)
                maxProfit = pist;
            //cout<<"\nmaxProfit at iteration "<<i<<" = "<<maxProfit;
        }

        return maxProfit;
    }
};
