#include<iostream>
using namespace std;

int main(){
    int a[3];
    int b[3];
    int temp;
    for(int i=0; i<3; i++){
        cin>>a[i];
    }
    for(int i=0; i<3; i++){
        b[i]=a[i];
    }
    for(int i=0; i<3; i++){
       for(int j=i+1;j<3;j++){
        if(a[i]>a[j]){
            temp=a[i];
			a[i]=a[j];
			a[j]=temp;
			}
		}
    }
    for(int i=0; i<3; i++){
        cout<<a[i]<<endl;
    }
    cout<<endl;
    for(int i=0; i<3; i++){
        cout<<b[i]<<endl;
    }   
    return 0;
}