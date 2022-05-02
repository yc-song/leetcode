#include <cmath>
class Solution {
public:
    int count =1;
    double myPow(double x, long long n) {
        if (n>=0&& x!=1 && x!=(-1)){
        return __mypow(x, x, n);}
        else if (x==1) return 1;
        else if (x==-1) {
            if (n%2 ==0 ) return 1;
            else return -1;
        }
        else if (n<0) return 1/__mypow(x,x,-n);
        return 0;
    }
    double __mypow(double x, double y, long long n){
        if (n>=2){
        if (n%2 ==0) return __mypow(y, y*y, n/2);
        else if (n%2==1) return y*__mypow(y, y*y, n/2);
        }
        else if (n==1) return y;
        else if (n==0) return 1;
    
        return 0;
    }
   
};