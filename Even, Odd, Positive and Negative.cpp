#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    cout<<"Even: ";
    int k=0;
    int com=0;
    while(k<n){
        if(a[k]%2==0){
            com=com+1;;
        }
        k++;
    }
    cout<<com<<endl;
    cout<<"Odd: ";
    k=0;
    com=0;
    while(k<n){
        if(a[k]%2!=0){
            com=com+1;;
        }
        k++;
    }
    cout<<com<<endl;  
    cout<<"Positive: ";
    k=0;
    com=0;
    while(k<n){
        if(a[k]>0){
            com=com+1;;
        }
        k++;
    }
    cout<<com<<endl;
    cout<<"negative: ";
    k=0;
    com=0;
    while(k<n){
        if(a[k]<0){
            com=com+1;
        }
        k++;
    }
    cout<<com<<endl;
    return 0;
}