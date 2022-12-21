#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int a,b;
        cin>>a>>b;
        unsigned long long c[max(a,b)+1];
        for(int i=0;i<=max(a,b);i++){
            c[i] = ((a^i)+(b^i));
        }
        cout<<*min_element(c, c + max(a,b)+1)<<"\n";
    }
    return 0;
}