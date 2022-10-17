#include<iostream>
#include <iomanip>
using namespace std;

int main(){
    double num;
    cout << fixed << setprecision(3);
    cin>>num;
    if(float(num-int(num))==0){
        cout<<"int "<<int(num);
    } else {
        cout<<"float "<<int(num)<<" "<<float(num-int(num));
    }
}