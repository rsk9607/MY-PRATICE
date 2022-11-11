#include<bits/stdc++.h>
using namespace std;

// int fib(int n){
//     if(n==1){
//         return 0;
//     } else if(n==2){
//         return 1;
//     } else {
//         return fib(n-1)+fib(n-2);
//     }
// }

// int main(){
//     int n;
//     cin>>n;
//     cout<<fib(n);
// }

int main(){
    int n;
    cin>>n;
    long long int a[n]= {0,1};
    for(int i=2; i<n;i++){
        a[i]=a[i-1]+a[i-2];
    }
    cout<<a[n-1];
}