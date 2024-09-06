class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n=nums.size(),i;
        unordered_map<int,int> m;
        for(i=0;i<n;i++){
            m[nums[i]]++;

            if(m[nums[i]]>1) return true;
        }
        return false;
    }
};
