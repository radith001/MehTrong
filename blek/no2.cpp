#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Array 2 dimensi sesuai tabel nilai
    int nilai[2][10] = {
        {50, 55, 45, 35, 70, 85, 90, 20, 45, 60},
        {65, 56, 60, 80, 75, 35, 25, 60, 70, 75}
    };

    // Cetak tabel nilai
    cout << "TABEL NILAI:" << endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 10; j++) {
            cout << nilai[i][j] << " ";
        }
        cout << endl;
    }

    // Mencari nilai terkecil menggunakan index sequential
    int terkecil = nilai[0][0];
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 10; j++) {
            if (nilai[i][j] < terkecil) {
                terkecil = nilai[i][j];
            }
        }
    }

    cout << "\nNilai terkecil: " << terkecil << endl;

    return 0;
}