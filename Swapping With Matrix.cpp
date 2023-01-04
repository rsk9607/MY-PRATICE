#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,x,y;
    cin>>n>>x>>y;
    int a[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>a[i][j];
        }
    }
    int temp;
    for(int i=0;i<n;i++){
        temp =a[x-1][i];
        a[x-1][i]=a[y-1][i];
        a[y-1][i]=temp;
    }
        for(int i=0;i<n;i++){
        temp =a[i][x-1];
        a[i][x-1]=a[i][y-1];
        a[i][y-1]=temp;
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<a[i][j]<<" ";
        }
        cout<<"\n";
    }
}