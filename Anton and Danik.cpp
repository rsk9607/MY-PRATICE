#include<iostream>
#include <string>
using namespace std;

int main(){
    int n;
    cin>>n;
    string game;
    cin>>game;
    int a=0;
    int d=0;
    for(int j=0; j<n; j++){
        if(game[j]=='A'){
            a++;
        } else if(game[j]=='D'){
            d++;
        }
    }
    if(a>d){
        cout<<"Anton";
    } else if(a<d){
        cout<<"Danik";
    } else if(a==d){
        cout<<"Friendship";
    }
    return 0;
}