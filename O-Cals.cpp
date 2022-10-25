#include<bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    int n, k;
    n = s.length();
    for (int i = 0; i < n; i++) {
        if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
            k = i + 1;
            break;
        }
    }
    int a, b;
    string s1, s2;
    for (int j = 0; j < k; j++) {
        s1 = s1 + s[j];
    }
    for (int j = k + 1; j < n; j++) {
        s2 = s2 + s[j];
    }
    a = stoi(s1);
    b = stoi(s2);
    if (s[k-1] == '+') {
        cout << a + b;
    } else if (s[k-1] == '-') {
        cout << a - b;
    } else if (s[k-1] == '*') {
        cout << a * b;
    } else if (s[k-1] == '/') {
        cout << a / b;
    }

}