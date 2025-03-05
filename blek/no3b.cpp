#include <iostream>
#include <vector>
using namespace std;

// Fungsi Bubble Sort
void bubbleSort(vector<char>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    string nama = "Yesayanto Damar Natanael";
    vector<char> arr(nama.begin(), nama.end());

    cout << "Array sebelum diurutkan (Bubble Sort):" << endl;
    for (char c : arr) {
        cout << c;
    }
    cout << endl;

    bubbleSort(arr);

    cout << "Array setelah diurutkan (Bubble Sort):" << endl;
    for (char c : arr) {
        cout << c;
    }
    cout << endl;

    return 0;
}