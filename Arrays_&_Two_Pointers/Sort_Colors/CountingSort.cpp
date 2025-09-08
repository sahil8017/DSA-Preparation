#include<bits/stdc++.h>
using namespace std;

void sortColors(vector<int>& nums){
    int low = 0, mid = 0, high = 0;
    for(int i = 0; i < nums.size(); i++){
        if(nums[i] == 0) low++;
        else if(nums[i] == 1) mid++;
        else high++;
    }
    int index = 0;
    for(int i = 0; i < low; i++){
        nums[index] = 0;
        index++;
    }
    for(int i = 0; i < mid; i++){
        nums[index] = 1;
        index++;
    }
    for(int i = 0; i < high; i++){
        nums[index] = 2;
        index++;
    }    
}

int main(){
    vector<int> values = {2,0,2,1,1,0};
    sortColors(values);
    for(int i = 0; i < values.size(); i++){
        cout << values[i] << " ";
    } 
}
