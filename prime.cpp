#include<iostream>
using namespace std;

int main(){
    int a;
    cin>>a;
    int i=2;
    while(i<=a){
        if(a%i==0 && i!=a){
            cout<<"NO";
            break;
        }else if(a%i==0 && i==a){
            cout<<"YES";
        } 
        i++;
    }
    return 0;
}
