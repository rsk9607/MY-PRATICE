// #include<iostream>
// using namespace std;

// int prime(int a){
//     int i=2;
//     while(i<=a){
//         if(a%i==0 && i!=a){
//             return 0;
//             break;
//         }else if(a%i==0 && i==a){
//             return 1;
//         } 
//         i++;
//     }
// }

// int main(){
//     int t;
//     cin>>t;
//     while(t--){
//         int a;
//     cin>>a;
//     int i=2;
//     while(i<=a){
//         if(a%i==0 && i!=a){
//             cout<<"NO \n";
//             break;
//         }else if(a%i==0 && i==a){
//             cout<<"YES \n";
//         } 
//         i++;
//     }
//     }
    
//     return 0;
    
// }

// A optimized school method based C++ program to check
// if a number is prime
#include <bits/stdc++.h>
using namespace std;
 
bool isPrime(int n)
{
    // Corner cases
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
 
    // This is checked so that we can skip
    // middle five numbers in below loop
    if (n % 2 == 0 || n % 3 == 0)
        return false;
 
    // Using concept of prime number
    // can be represented in form of
    // (6*n + 1) or(6*n - 1) hence
    // we have to go for every multiple of 6 and
    // prime number would always be 1 less or 1 more than
    // the multiple of 6.
   
    /*
       1. Here i is of the form 5 + 6K where K>=0
       2. i+1, i+3, i+5 are even numbers (6 + 6K). N is not an even number
       3. Because N%2 and N%3 checks are done in the before step
       4. Hence i+1, i+3, i+5 can't be N's divisors.
       5. i+4 is 9 + 6K which is a 3 multiple.
       6. N is not a 3 multiple hence i+4 can't be it's divisor
       Hence we only check if N is a divisor of i or i+2.
    */
    for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
 
    return true;
}
 
// Driver Program to test above function
int main()
{
    int t;
    cin>>t;
    while(t--){
        int a;
        cin>>a;
        isPrime(a) ? cout << "YES\n" : cout << "NO\n";
    }
    return 0;
}