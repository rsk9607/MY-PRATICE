#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int x;
        int y;
        int n = 0;
        while(true){
            if((n+x)%y==0 and (n+y)%x==0){
                cout<<n<<"\n";
                break;
            } else{
                n++;
            }
        }
    }
    return 0;
}