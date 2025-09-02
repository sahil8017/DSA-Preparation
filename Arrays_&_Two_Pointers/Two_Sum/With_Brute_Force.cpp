// Brute Force(naive) Approach
#include<bits/stdc++.h>
using namespace std;
vector<int> twoSum(vector<int>& nums, int target){
    vector<int> result;
    int n = nums.size();
    for(int i = 0; i < n; i++){
        int remaining = target - nums[i];
        for(int j = i + 1; j < n; j++){
            if(nums[j] == remaining){
                return{i, j};
            }
        }
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
