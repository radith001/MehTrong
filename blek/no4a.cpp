#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> arr = {50, 55, 45, 35, 70, 85, 90, 20, 45, 60, 65, 56, 60, 80, 75, 35, 25, 60, 70, 75};

    int terbesar = arr[0];
    for (int i : arr) {
        if (i > terbesar) {
            terbesar = i;
        }
    }

    cout << "Nilai terbesar (Sekuensial): " << terbesar << endl;

    return 0;
}