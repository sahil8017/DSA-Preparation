#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    set<vector<int>> st;
    for(int i = 0; i < n; i++){
        int left = i + 1;
        int right = n - 1;
        while(left < right){
            int sum = nums[i] + nums[left] + nums[right];
            if(sum > 0) right--;
            else if(sum < 0) left++;
            else{
                st.insert({nums[i], nums[left], nums[right]});
                left++;
                right--;
                while(left < right && nums[left] == nums[left-1]) left++;
                while(left < right && nums[right] == nums[right+1]) right--;
            }
        }
    }
    return vector<vector<int>>(st.begin(), st.end());
}

int main(){
    vector<int> values = {-1,0,1,2,-1,-4};
    vector<vector<int>> result = threeSum(values);
    for(int i = 0; i < result.size(); i++){
        for(int j = 0; j < result[i].size(); j++){
            cout << result[i][j] << " ";
        }
    cout<<endl;
    }

}
