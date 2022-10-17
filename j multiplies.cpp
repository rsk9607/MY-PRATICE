#include<iostream>
using namespace std;

int main(){
    int a;
    int b;
    cin>>a>>b;
    if(float(a%b==0) || float(b%a==0)){
        cout<<"Multiples";
    } else {
        cout<<"No Multiples";
    }
    return 0;
}