// int main() {
//     int t;
//     int c;
//     int n = 0;
//     cin >> t;
//     while (t > 0) {
//         t--;
//         cin >> c;
//         int time = 0;
//         while ((c - n) != 0) {
//             if ((c - n) > 1 && (c - n) % 2 == 0 && (c - n) % 3 == 0) {
//                 n = n + 3;
//                 time++;
//             } else if ((c - n) > 1 && (c - n) % 3 == 0 && (c - n) % 2 != 0) {
//                 n = n + 3;
//                 time++;
//             } else if ((c - n) > 1 && (c - n) % 2 == 0 && (c - n) % 3 != 0 && (c - n) > 4) {
//                 n = n + 3;
//                 time++;
//             } else if ((c - n) > 1 && (c - n) % 2 == 0 && (c - n) % 3 != 0 && (c - n) < 4) {
//                 n = n + 2;
//                 time++;
//             } else if ((c - n) > 1 && (c - n) % 2 != 0 && (c - n) % 3 != 0) {
//                 n = n + 3;
//                 time++;
//             } else
//             if ((c - n) == 1) {
//                 n = n - 2;
//                 time++;
//             }
//         }
//          if (c == n) {
//                 cout << time<<endl;
//             }

//     }
//     return 0;
// }