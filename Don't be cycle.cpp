#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m;
    vector<vector<int>> edge;
    for (int i = 0; i < m; ++i) {
        vector<int> k;
        for (int j = 0; j < 2; ++j) {
            int x;
            cin >> x;
            k.push_back(x);
        }
        sort(k.begin(),k.end());
        edge.push_back(k);
    }
    sort(edge.begin(),edge.end());
    int count=0;
    for(int i=0; i<edge.size()-2;i++){
        if(edge[i][0]==edge[i+1][0]){
            if(edge[i+2][0]==edge[i][1] and edge[i+2][1]==edge[i+1][1]){
                count++;
            }
        }else{
            continue;
        }

    }
    cout<<count;
}

