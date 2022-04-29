/*
 * @lc app=leetcode id=835 lang=cpp
 *
 * [835] Image Overlap
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        vector<vector<int>> img1_padding(img1.size()*3-2,vector<int>(img1.size()*3-2,0));
        int s = img1.size();
        for (int i =0; i<s;i++){
            for (int j =0; j<s;j++){
                img1_padding[i+s-1][j+s-1]=img1[i][j];
            }
        }
        int max =0;
        int result =0;
        for (int i =0; i<s*2-1;i++){
            for (int j =0; j<s*2-1;j++){
                vector<vector<int>> *temp=new vector<vector<int>>;
                // cout<<"i and j: "<<i<<j<<endl;
                result = convolution(img2, img1_padding, i,j);
                if (result>max){
                    max=result;
                    
                }
            }
        }
        
   
    
        return max;
    }
    int convolution (vector<vector<int>>& img1, vector<vector<int>>& img2, int l, int r){
        int result=0;
        for (int i =0; i<img1.size();i++){
            for (int j =0; j<img1[0].size();j++){
                
                result+=img1[i][j]*img2[i+r][j+l];
            }
        }
       
        return result;
    }

};


