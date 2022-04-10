#include <map>
#include <string>
class Solution {
public:
    int firstUniqChar(std::string s) {
        for (int i=0; i<s.size();i++){
            ret=myhashmap.insert ( std::pair<char,int>(s[i],i));
            if (ret.second == false) myhashmap[s[i]]=100000;
                
            
        }
        for (it = myhashmap.begin(); it != myhashmap.end(); it++){
    
        if (it->second < 100000) {
            if (min == nullptr) min = &(it -> second);
            else if (*min>it->second) *min = it -> second;

    }
    }
    if (min == nullptr) return -1;
    else return *min;
    }
private:
std::map<char, int> myhashmap;
std::pair<std::map<char, int>::iterator, bool> ret;
std::map<char, int>::iterator it;
int* min = nullptr;
};