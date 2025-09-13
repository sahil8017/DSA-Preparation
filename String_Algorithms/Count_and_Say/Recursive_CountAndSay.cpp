#include<bits/stdc++.h>
using namespace std;

string count(string s){
    string result = "";
    for(int i = 0; i < s.length(); i++){
        int count = 1;
        while(i + 1 < s.length() && s[i] == s[i + 1]){
            count++;
            i++;
        }
        result += to_string(count) + s[i];
    }
    return result;
}
string countAndSay(int n){
    if(n == 1) return "1";
    return count(countAndSay(n-1));
}

int main(){
    int n = 4;
    cout << countAndSay(n) << endl;
}
