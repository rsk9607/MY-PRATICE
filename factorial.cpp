#include<bits/stdc++.h>

using namespace std;

int main() {
    int n, t;
    cin >> t;
    long long int temp;
    while (t--) {
        cin >> n;
        temp = 1;
        for (int j = 1; j <= n; j++) {
            temp *= j;

        }
        cout << temp << endl;
    }
    return 0;
}


