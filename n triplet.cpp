#include <iostream>
using namespace std;

#define int long long 

signed main() {
	int test;
	cin>>test;
	while(test--){
	    int mun;
	    cin>>mun;
	    int f_1=0,f_2=0;
	    for(int i=2;i*i<mun;i++){
	        if(mun%i==0){
	            f_1=i;
	            f_2=mun/i;
	            break;
	        }
	    }
	    if(f_1 && f_2 && f_1!=f_2){
	        cout<<1<<" "<<f_1<<" "<<f_2<<endl;
	    }
	    else{
	        cout<<-1<<endl;
	    }
	}
	return 0;
}