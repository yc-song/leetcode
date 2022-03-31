#include <string>
#include <map>
#include <math.h>
class Solution {
public:
std::string sub_s;
    
    bool hasAllCodes(std::string s, int k) {
        int target = pow(2,k);
        for (int i =0; i+k<=s.size();i++){
            sub_s = s.substr(i,k);
            ret=myhashmap.insert ( std::pair<std::string,int>(sub_s,1));
            if (ret.second == true){
                count++;
            }
            if (count == target) return true;
            
        }
        
        return false;
    }
private:
std::map<std::string, int> myhashmap;
std::pair<std::map<std::string, int>::iterator, bool> ret;
int count = 0;
};