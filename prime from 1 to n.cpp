#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a=2;
    rep:
    while(a<=n){
        int i=2;
        while(i<=a){
            if(a%i==0 && i!=a){
                a++;
                goto rep;
            }else if(a%i==0 && i==a){
                cout<<a<<" ";
            } 
            i++;
        }
        a++;
    }
    return 0;
}