// HashMap Approach
#include<bits/stdc++.h>
using namespace std;
vector<int> twoSum(vector<int>& nums, int target){
    int n = nums.size();
    unordered_map<int,int>mpp;
    for(int i = 0; i < n; i++){
        int remaining = target - nums[i];
        if(mpp.count(remaining)){
            return {mpp[remaining], i};
        }
        mpp[nums[i]] = i;
    }
    return{};
}

int main(){
    vector<int> values = {2,7,11,15};
    vector<int> result = twoSum(values, 22);
    for(int i = 0; i < result.size(); i++){
        cout<<result[i]<<" ";
    }
    cout<<endl;
    return 0;
}
