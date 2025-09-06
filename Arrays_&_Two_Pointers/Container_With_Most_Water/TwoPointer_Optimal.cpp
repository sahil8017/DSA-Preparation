#include<bits/stdc++.h>
using namespace std;
int maxArea(vector<int>& height){
    
    int h = height.size();
    int left = 0;
    int right = h - 1;
    int res = 0;
    while(left <= right){
        int area = (right - left) * min(height[left], height[right]);
        res = max(area, res);
        
        if(height[left] < height[right]){
            left++;
        }
        else{
            right--;
        }
    }
    return res;
}

int main(){
    vector<int> values = {1,8,6,2,5,4,8,3,7};
    cout<<maxArea(values);
    return 0;
}
