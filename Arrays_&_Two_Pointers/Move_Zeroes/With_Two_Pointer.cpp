#include<bits/stdc++.h>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int nonzerolastelt = 0;
    int n = nums.size();
    
    // Move non-zero elements to the front
    for (int i = 0; i < n; i++) {
        if (nums[i] != 0) {
            nums[nonzerolastelt++] = nums[i];
        }
    }
    
    // Fill the remaining positions with zeroes
    for (int i = nonzerolastelt; i < n; i++) {
        nums[i] = 0;
    }
}

int main() {
    vector<int> values = {0, 1, 0, 3, 12};
    moveZeroes(values);
    
    // Print the modified array
    for (int i = 0; i < values.size(); i++) {
        cout << values[i] << " ";
    }
    cout << endl;
    
    return 0;
}
