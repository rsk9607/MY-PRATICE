#include<bits/stdc++.h>
using namespace std;
 
#define int long long 
 
signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        int x=a[0];
        sort(a,a+n);
        for(int i=0;i<n;i++){
            if(a[i]>x){
                int c=a[i]-x;
                if(c%2==0){
                    x=x+c/2;
                }
                else{
                    x=x+1+c/2;
                }
            }
            else{
                continue;
            }
        }
        cout<<x<<endl;
    }
    return 0;
}