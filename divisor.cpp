#include<iostream>
using namespace std;

int main(){
    int p;
    int i=1;
    cin>>p;
    while(i<=p){
        if(p%i==0){
            cout<<i<<endl;
        }
        i++;
    }
    return 0;
}

