#include<iostream>
using namespace std;
 
int main(){
    long long t;
    cin>>t;
    while(t>0){
        t--;
        int a;
        long b;
        cin>>a>>b;
        long long k;
        k=int((b*(b+1))/2)-(((a-1)*a)/2);
        cout<<k<<endl;
    }
    return 0;
}