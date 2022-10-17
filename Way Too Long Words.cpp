#include<iostream>
#include<string>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t>0){
        string word;
        cin>>word;
        int l=word.length();
        if(l<=10){
            cout<<word<<endl;
        } else{
        cout<<word[0]<<word.length()-2<<word[l-1]<<endl;
        }
        t--;
    }
    return 0;
}