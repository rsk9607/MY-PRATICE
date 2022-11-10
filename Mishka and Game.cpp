#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    int m=0;
    int c=0;
    while(n--){
        int x;
        int y;
        cin>>x>>y;
        if(x>y){
            m = m+2;
        } else if(x<y){
            c = c+2;
        } else if(x==y){
            c= c+1;
            m= m+1;
        }
    }
    if(m>c){
        cout<<"Mishka \n";
    } else if(m<c){
        cout<<"Chris \n";
    } else if(m==c){
        cout<<"Friendship is magic!^^ \n";
    }
    return 0;
}