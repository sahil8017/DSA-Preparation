#include <bits/stdc++.h>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    if (n == 0) return 0;

    int left = 0;
    for (int right = 1; right < n; ++right) {
        if (nums[right] != nums[left]) {
            ++left;
            nums[left] = nums[right];
        }
    }
    return left + 1;
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
