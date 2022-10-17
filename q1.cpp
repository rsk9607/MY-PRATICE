#include <iostream>
using namespace std;

int main() {
    int t;
    int a;
    int b;
    cin>>t;
    while(t>0){
        cin>>a>>b;
        t--;
        if(a==b){
            cout<<"Yes";
        }else
            if(a!=b){
                cout<<"No";
        }
        if(a!=b){
            if(a>b){
                b=b+a-b;
            }else{
                a=a+b-a;
            }
        }
    }
	return 0;
}