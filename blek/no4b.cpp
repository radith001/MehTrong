#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> arr = {50, 55, 45, 35, 70, 85, 90, 20, 45, 60, 65, 56, 60, 80, 75, 35, 25, 60, 70, 75};

    // Array harus diurutkan untuk pencarian biner
    sort(arr.begin(), arr.end());

    int terkecil = arr[0]; // Nilai terkecil ada di indeks pertama setelah diurutkan

    cout << "Nilai terkecil (Biner): " << terkecil << endl;

    return 0;
}