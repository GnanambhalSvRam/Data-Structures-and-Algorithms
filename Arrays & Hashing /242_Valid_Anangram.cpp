class Solution {
public:
    bool isAnagram(string s, string t) 
    {
        if(s.length() != t.length() || 
           (s.length() == 1 && t.length() == 1 && s[0] != t[0]))
            return false;
        
        unordered_map<char,int> smap, tmap;
        for(int i=0; i<s.length(); i++)
        {
            char key = s[i];
            if(smap.find(key) == smap.end())
                smap[key] = 1;
            else
                smap[key] += 1;
        }

        for(int i=0; i<t.length(); i++)
        {
            char key = t[i];
            if(tmap.find(key) == tmap.end())
                tmap[key] = 1;
            else
                tmap[key] += 1;
        }

        for(auto itr = smap.begin(); itr!=smap.end(); itr++)
        {
            char key = itr->first;
            if(tmap.find(key) == tmap.end() || tmap[key] != smap[key])
                return false;
        }

        return true;

    }
};
