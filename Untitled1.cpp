#include <iostream>
using namespace std;

int main() {
    int a;
    int b;
    int t;
    cin>>t;
    while(t>0){
        int i=0;
        cin>>a>>b;
        t--;
        while(a!=b){
            if(a>b){
                while(a!=b){
                    b=b+2;
                    i++;
                }
            }
            if(a<b){
                while(a!=b){
                    a=a+1;
                    i++;
                }
            }
        }
        if(a==b){
            cout<<i<<endl;
        } 
    }
	return 0;
}
