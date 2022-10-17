#include<iostream>

using namespace std;



int main() {
    int p;
    int q = 0;
    int t;
    cin >> t;
    while (t > 0) {
        t--;
        cin >> p;
        q = p / 3;
        if (p % 3 != 0) {
            q++;
        } 
        if (p == 1) {
            q = 2;
        }

        cout << q << endl;
    }
}