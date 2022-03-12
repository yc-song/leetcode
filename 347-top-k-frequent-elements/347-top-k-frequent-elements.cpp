#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
bool cmp(const pair<int, int>& a, const pair<int, int>& b);
class Solution {
public:

    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counting;
        map<int, int>::iterator iter;
        counter(counting, nums);
        vector<pair<int, int>> vec(counting.begin(), counting.end());
        sort(vec.begin(), vec.end(), cmp);
        int c = 0;
        vector<int> ans= {};
        while (c<k) {
            auto i = vec[c++];
            ans.push_back(i.first);
        }
        return ans;
    }
    void counter(map<int, int>& counting, vector<int> &nums) {
        int len = nums.size();
        for (int i = 0; i < len; i++) {
            counting[nums[i]]++;
        }
    }

private:
    friend bool cmp(const pair<int, int>& a, const pair<int, int>& b);

};
bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
    if (a.second == b.second) return a.first > b.first;
    return a.second > b.second;
}