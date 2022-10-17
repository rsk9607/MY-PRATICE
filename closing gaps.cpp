#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t>0){
        t--;
        int n;
        cin>>n;
        int a[1000];
        int i=0;
        while(i<n){
            cin>>a[i];
            i++;
        }
        i=0;
        while(i<n){
            cout<<a[i];
        }
    return 0;
}
