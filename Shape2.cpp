#include<iostream>
using namespace std;

int main(){
    int n;
    int j=1;
    cin>>n;
    while(n>0){
        for(int i=n-1; i>0; i--){
            cout<<" ";
        }
        int k=2*j-1;
        while(k>0){
            cout<<"*";
            k--;
        }
        n--;
        j++;
        cout<<"\n";
    }
}