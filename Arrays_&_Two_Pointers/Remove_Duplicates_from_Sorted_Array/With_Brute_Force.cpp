#include <bits/stdc++.h>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    vector<int> result;
    result.push_back(nums[0]);
    for(int i = 1; i < n; i++){
        if(nums[i] != nums[i-1]){
            result.push_back(nums[i]);
        }
    }
    
    for(int i = 0; i < result.size(); i++){
        nums[i] = result[i];
    }
    return result.size();
}

int main() {
    vector<int> values = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    
    int newLength = removeDuplicates(values);

    cout << "New length: " << newLength << endl;
    cout << "Modified array: ";
    for (int i = 0; i < newLength; ++i) {
        cout << values[i] << " ";
    }
    cout << endl;

    return 0;
}
