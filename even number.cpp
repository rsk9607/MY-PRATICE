#include<iostream>
using namespace std;

int main(){
    int k;
    cin>>k;
    if(k==1){
        cout<<"-1"<<endl;
    } else {
        int i=2;
        while(i<=k){
            cout<<i<<endl;
            i=i+2;
        }
    }
    return 0;
}