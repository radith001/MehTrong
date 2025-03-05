#include <iostream>
#include <vector>
using namespace std;

// Fungsi untuk partisi dalam Quick Sort
int partisi(vector<char>& arr, int rendah, int tinggi) {
    char pivot = arr[tinggi];
    int i = rendah - 1;

    for (int j = rendah; j < tinggi; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[tinggi]);
    return i + 1;
}

// Fungsi Quick Sort
void quickSort(vector<char>& arr, int rendah, int tinggi) {
    if (rendah < tinggi) {
        int pi = partisi(arr, rendah, tinggi);
        quickSort(arr, rendah, pi - 1);
        quickSort(arr, pi + 1, tinggi);
    }
}

int main() {
    string nama = "Yesayanto Damar Natanael";
    vector<char> arr(nama.begin(), nama.end());

    cout << "Array sebelum diurutkan (Quick Sort):" << endl;
    for (char c : arr) {
        cout << c;
    }
    cout << endl;

    quickSort(arr, 0, arr.size() - 1);

    cout << "Array setelah diurutkan (Quick Sort):" << endl;
    for (char c : arr) {
        cout << c;
    }
    cout << endl;

    return 0;
}