
#include<bits/stdc++.h>
using namespace std;
string countAndSay(int n){
    if(n == 1) return "1";
    string result = "1";
    for(int i = 1; i < n; i++){
        int count = 1;
        char curcount = result[0];
        string temp = "";
        for(int j = 1; j < result.length(); j++){
            if(result[j] == curcount){
                count++;
            }else{
                temp += to_string(count);
                temp.push_back(curcount);
                curcount = result[j];
                count = 1;
            }
        }
        temp += to_string(count);
        temp.push_back(curcount);
        
        result.swap(temp);
    }
    return result;
}

int main(){
    int n = 4;
    cout << countAndSay(n) << endl;
}
