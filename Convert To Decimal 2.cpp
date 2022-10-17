#include<iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t>0){
        t--;
        int n;
        cin>>n;
        int k=0;
        while(n!=0){
            if(n%2==1){
                k++;
            }
            n=n/2;
        }
        int i=k-1;
        int sum = 0;
        while(i>=0){
            sum=sum+pow(2.0, i);
            i--;
        }
        cout<<sum<<endl;
    }
}