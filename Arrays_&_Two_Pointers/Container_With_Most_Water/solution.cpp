#include<bits/stdc++.h>
using namespace std;

int maxArea(vector<int>& height){
    int n = height.size();
    int res = 0;
    
    for(int i = 0; i < n; i++){
        for(int j = i + 1; j < n; j++){
            int area = (j - i) * min(height[i], height[j]);
            res = max(res, area);
        }
    }
    return res;
}

int main(){
    vector<int> values = {1,8,6,2,5,4,8,3,7};
    int s = maxArea(values);
    cout << s << endl;
    return 0;
}
