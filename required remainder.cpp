#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int x,y,n;
        cin>>x>>y>>n;
        int q = n/x;
        int r = n%x;
        if(y<r){
            cout<<(q*x)+y<<"\n";
        } else if(y>r){
            cout<<((q-1)*x)+y<<"\n";
        } else {
            cout<<n<<"\n";
        }
    }
    return 0;
}