#include <iostream>
#include <vector>
using namespace std;
using std::swap;
int findKthelement(vector<int>& nums, int k);
int finder(vector<int>& nums, int start, int end, int k);
int partition(vector<int>& nums, int start, int end);

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        k--;
        int len = nums.size();
        return finder(nums, 0, len-1, k);
    }
    int finder(vector<int>& nums, int start, int end, int k) {
        if (start == end) return nums[start];
        while (start < end) {
            int q = partition(nums, start, end);
            if (k > q) return finder(nums, q + 1, end, k);
            else if (q > k) return finder(nums, start, q - 1, k);
            else return nums[q];
        }
        return 0;
    }
    int partition(vector<int>& nums, int start, int end) {
        int j = start;
        for (int i = start + 1; i < (end + 1); i++) {
            if (nums[i] > nums[start]) {
                j++; //omit later
                swap(nums[j], nums[i]);
            }
        }
    swap(nums[start], nums[j]);
    return j;
    }

  
};