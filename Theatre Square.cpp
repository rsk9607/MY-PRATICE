#include<bits/stdc++.h>
using namespace std;

int main(){
    int m,n,a;
    cin>>n>>m>>a;
    unsigned long long int k;
    k=(m*n)/(a*a);
    unsigned long long int l=0;
    if((m*n)%(a*a)!=0){
        while(a*l<m){
            l++;
        }
    }
    k=k+l;
    cout<<k;
}