// Two Pointer Approach
#include<bits/stdc++.h>
using namespace std;
vector<int> twoSum(vector<int>& nums, int target){
    int n = nums.size();
    int left = 0;
    int right = n - 1;
    while(left < right){
        int sum = nums[left] + nums[right];
        if(sum == target){
            return{left, right};
        }
        else if(sum > target){
            right--;
        }
        else{
            left++;
        }
    }
    return {};
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
