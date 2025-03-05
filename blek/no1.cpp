#include <iostream>
#include <string>
using namespace std;

int main() {
    string nama = "Yesayanto Damar Natanael";
    int baris = (nama.length() + 4) / 5; // Menghitung jumlah baris
    char array_nama[baris][5];

    // Mengisi array 2 dimensi
    int index = 0;
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < 5; j++) {
            if (index < nama.length()) {
                array_nama[i][j] = nama[index];
                index++;
            } else {
                array_nama[i][j] = ' '; // Mengisi spasi jika nama sudah habis
            }
        }
    }

    // Cetak per baris
    cout << "Cetak per baris:" << endl;
    for (int i = 0; i < baris; i++) {
        for (int j = 0; j < 5; j++) {
            cout << array_nama[i][j];
        }
        cout << endl;
    }

    // Cetak per kolom
    cout << "\nCetak per kolom:" << endl;
    for (int j = 0; j < 5; j++) {
        for (int i = 0; i < baris; i++) {
            cout << array_nama[i][j];
        }
        cout << endl;
    }

    return 0;
}