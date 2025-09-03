// InPlace_TwoPointer
#include<bits/stdc++.h>
using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    vector<int> temp;
    temp.reserve(m+n);
    
    for(int i = 0; i < m; i++){
        temp.push_back(nums1[i]);
    }
    for(int j = 0; j < n; j++){
        temp.push_back(nums2[j]);
    }
    
    sort(temp.begin(), temp.end());
    for(int i = 0; i < temp.size(); i++){
        nums1[i] = temp[i];
    }    
}

int main(){
    vector<int> value1 = {1,2,3,0,0,0};
    vector<int> value2 = {2,5,6};
    merge(value1, 3, value2, 3);
    for(int i = 0; i < value1.size(); i++){
        cout << value1[i] << " ";
    }
    cout<<endl;
    return 0;
}
