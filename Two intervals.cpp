#include<iostream>
using namespace std;

int main(){
    int l1;
    int r1;
    int l2;
    int r2;
    cin>>l1>>r1>>l2>>r2;
    if(l1<=l2 && l2<=r1 && l1<=r2 && r2<=r1 ){
        cout<<l2<<" "<<r2;
    } else if(l2<=l1 && l1<=r2 && l2<=r1 && r1<=r2 ){
        cout<<l1<<" "<<r1;
    } else if(l1<=l2 && l2<=r1){
        cout<<l2<<" "<<r1;
    } else if(l1<=r2 && r2<=r1){
        cout<<l1<<" "<<r2;
    } else {
        cout<<"-1";
    }
    return 0;
}