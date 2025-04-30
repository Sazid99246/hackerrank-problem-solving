#include <bits/stdc++.h>
using namespace std;


int main() {

    int n, q;
    cin >> n >> q;
    int** pt = new int*[n];
    
    for (int i = 0; i < n; i++)
    {
        int k;
    
        cin >> k;
        pt[i] = new int[k];
    
        for (int j = 0; j < k; j++)
        {
            int val;
            cin >> val;
            pt[i][j] = val;
        }
    }
    
    for (int a = 0; a < q; a++)
    {
        int i = 0;
        cin >> i;
        int j = 0;
        cin >> j;
    
        cout << pt[i][j] << endl;
    }
    return 0;
    }