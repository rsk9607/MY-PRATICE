#include<iostream>
#include<bits/stdc++.H>
using namespace std;
 
int main(){
    int t;
    cin>>t;
    while(t>0){
        t--;
        unsigned long long int a;
        unsigned long long int b;
        cin>>a>>b;
        unsigned long long int ma;
        unsigned long long int mb;
        mb = max(a,b);
        ma = min(a,b);
        unsigned long long int  k;
        k=((ma+mb)*(mb-ma+1))/2;
        cout<<k<<endl;
    }
    return 0;
}