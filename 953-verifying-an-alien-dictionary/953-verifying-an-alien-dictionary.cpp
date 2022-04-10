#include <iostream>
#include <map>
#include <vector>
class Solution {
public:
std::map<char, char> alien_to_human;
std::vector<int>::iterator it;

bool isAlienSorted(std::vector<std::string>& words, std::string order) {
    char alphabet='a';
    for (char c:order){
        alien_to_human[c]=alphabet++;
    }
    for (std::string &word:words){
        for (char& c:  word){
            c = alien_to_human[c];
        }
    }
    for (int i = 0; i < words.size()-1; ++i) {
        for (int j = 0; j < words.size() - 1-i; ++j) {
            if (words[j] > words[j + 1]) {
                return false;
            }
        }
    }
    return true;
}
};
