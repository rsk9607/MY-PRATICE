#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[2][n];
    for(int i=0;i<2;i++){
        for(int j=0;j<n;j++){
            cin>>a[i][j];
        }
    }
    for(int i=1;i>=0;i--){
        for(int j=0;j<n;j++){
            cout<<a[i][j]<<" ";
        }
    }
    return 0;
}