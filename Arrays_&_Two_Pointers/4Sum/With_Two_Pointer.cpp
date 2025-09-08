#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> fourSum(vector<int>& nums, int target) {
    
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> ans;
    
    for(int i = 0; i < n; i++){
        if(i > 0 && nums[i] == nums[i-1]) continue;
        for(int j = i + 1; j < n; j++){
            if(j > i + 1 && nums[j] == nums[j-1]) continue;
            int left = j + 1;
            int right = n - 1;
            while(left < right){
                long long sum = (long long) nums[i] + nums[j] + nums[left] + nums[right];
                
                if(sum > target){
                    right--;
                }
                else if(sum < target){
                    left++;
                }
                else{
                    vector<int> temp = {nums[i],nums[j],nums[left],nums[right]};
                    ans.push_back(temp);
                    
                    while(left < right && nums[left] == nums[left+1]) left++;
                    while(left < right && nums[right] == nums[right-1]) right--;
                    
                    left++;
                    right--;
                }
            }
        }
    }
    return ans;
}

int main(){
    vector<int>values= {1,0,-1,0,-2,2};
    vector<vector<int>> result = fourSum(values, 0);
    for(int i = 0; i < result.size(); i++){
        for(int j = 0; j < result[i].size(); j++){
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
