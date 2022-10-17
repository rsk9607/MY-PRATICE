#include<bits/stdc++.h>
using namespace std;

int main(){
    int a[5][5];
    int b;
    int c;
    int k=0;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> a[i][j];
        }
    }
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if(a[i][j]==1){
                c=i;
                b=j;
            }
        }
    }
    // cout<<c<<b;
    while(c<2){
        c++;
        k++;
    }
    while(c>2){
        c--;
        k++;
    }
    while(b<2){
        b++;
        k++;
    }
    while(b>2){
        b--;
        k++;
    }    
    cout<<k;
}
