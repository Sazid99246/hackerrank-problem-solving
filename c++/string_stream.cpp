#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string s;
    cin >> s;

    for (char c : s)
    {
        if (c == ',')
        {
            cout << '\n';
        }
        else
        {
            cout << c;
        }
    }

    return 0;
}
