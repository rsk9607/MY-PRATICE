#include<iostream>
#include<vector>
using namespace std;

int main(){
    int d;
    int sumtime;
    int min;
    int max;
    cin>>d;
    int i=d;
    int l=0;
    while(d>=0){
         if(d>0){
        cin>>sumtime;
        cin>>d;
        l=l+sumtime;
    }else if(d=0){
        cin>>sumtime;
        d--;
        l=l+sumtime;
    }
    }
    cin>>min;
    cin>>max;

    // your final out
    int k;
    k=l/i;

    // your run operation
    if(k>=min && k<max){
        cout<<"YES"<<endl;
        cout<<d+1<<" ";
        cout<<k+1;
    }else{
        cout<<"NO";
    }
    return 0;
}