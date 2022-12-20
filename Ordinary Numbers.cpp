#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        int c=0;
        int i=1;
        while(i<=n){
            set<int> a;
            int k=i;
            while(k>0){
                a.insert(k%10);
                k = k/10;
            }
            if(a.size()==1){
                c++;
            }
            i = i+1;
        }
        cout<<c<<"\n";
    }
}