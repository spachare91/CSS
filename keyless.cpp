#include<bits/stdc++.h>

using namespace std;

int main(){
    string s="attack at once";
    int n=2;

    for(int i=0;i<n;i++){
        for(int j=i;j<s.size();j+=n){
            cout<<s[j]<<" ";
        }
    }
    cout<<endl;
    return 0;

}