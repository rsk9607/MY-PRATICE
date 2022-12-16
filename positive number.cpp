#include<iostream>
using namespace std;

int main(){
    char a;
    cout<<"Do you want to add number(y/n)";
    cin>>a;
    int sum=0;
    while(a=='y'){
        cout<<"entry a number: ";
        int k;
        cin>>k;
        if(k>0){
            sum = sum + k;
        }
        cout<<"Do you want to add number(y/n)";
        cin>>a;
    }
    if(a=='n'){
        cout<<"Your sum is "<<sum;
    }
    return 0;
}
