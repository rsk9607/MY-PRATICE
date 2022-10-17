#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    int max=a[0];
    int j=0;
    while(j<n){
        if(a[j]>max){
            max=a[j];
        }
        j++;
    }
    cout<<max;
    return 0;
}