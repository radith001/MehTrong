#include <iostream>

using namespace std;

int main() {
Game:
    int apasaja;
    int karakter;
    int pilihan;
    int health = 100;
    int healthmusuh = 100;
    int kondisiPermainan;
    int subMenu;

	#ifdef _WIN32
    	system("CLS");
	#else
    	system("clear");
	#endif

    cout << " ____      _       _ _____ ____  __        ___    ____  ____  ___ ___  ____" << endl;
    cout << "|  _ \\    / \\     | | ____/ ___| \\ \\      / / \\  |  _ \\|  _ \\|_ _/ _ \\|  _ \\ " << endl;
    cout << "| |_) |  / _ \\ _  | |  _|| |  _   \\ \\ /\\ / / _ \\ | |_) | |_) || | | | | |_) |" << endl;
    cout << "|  _ <  / ___ \\ |_| | |__| |_| |   \\ V  V / ___ \\|  _ <|  _ < | | |_| |  _ < " << endl;
    cout << "|_| \\_\\/_/   \\_\\___/|______\\____|    \\_/\\_/_/   \\_\\_| \\_\\_| \\_\\___\\___/|_| \\_\\" << endl;
    cout << "====================================================================================" << endl << endl;
    cout << "Selamat datang di Rajeg Warrior!!" << endl;
    cout << "Kalahkan Raja Hytam untuk memenangkan permainan ini." << endl << endl;
    cout << "Tekan 1 untuk melanjutkan" << endl;
    cin >> apasaja;

    #ifdef _WIN32
    	system("CLS");
	#else
    	system("clear");
	#endif

Balik1:
    cout << "Pilih karakter Anda:" << endl;
    cout << "1. Kesatria" << endl;
    cout << "2. Pemanah" << endl;
    cout << "3. Medis" << endl;
    cout << "Pilihan: ";
    cin >> karakter;

    #ifdef _WIN32
    	system("CLS");
	#else
    	system("clear");
	#endif

    if (karakter == 1) {
        cout << "Anda memilih Kesatria." << endl;
    } else if (karakter == 2) {
        cout << "Anda memilih Pemanah." << endl;
    } else if (karakter == 3) {
        cout << "Anda memilih Medis." << endl;
    } else {
        cout << "Pilihan tidak valid." << endl;
        goto Balik1;
    }

    do {
Balik2:
        cout << "\nPilihan tindakan:" << endl;
        cout << "1. Serang (-10 HP)" << endl;
        cout << "2. Memulihkan (+30 HP)" << endl;
        cout << "3. Beli Senjata" << endl;
        cout << "Pilihan: ";
        cin >> pilihan;

        #ifdef _WIN32
    		system("CLS");
		#else
    		system("clear");
		#endif

        if (pilihan == 1) {
            health -= 20;
            healthmusuh -= 10;
            cout << "Anda telah menyerang Raja Hytam dan Raja Hytam menyerang balik Anda" << endl;
            cout << "Sisa HP Anda: " << health << endl;
            cout << "Sisa HP Raja Hytam: " << healthmusuh << endl;
        } else if (pilihan == 2) {
            health += 30;
            cout << "Anda berhasil memulihkan diri. HP Anda sekarang: " << health << endl;
        } else if (pilihan == 3) {
Balik3:
            int senjata;
            cout << "List senjata yang tersedia:" << endl;
            cout << "1. Panah" << endl;
            cout << "2. Pedang" << endl;
            cout << "3. Catalyst" << endl;
            cout << "Pilihan senjata: ";
            cin >> senjata;

            #ifdef _WIN32
    			system("CLS");
			#else
    			system("clear");
			#endif

            if (senjata == 1) {
                cout << "Anda membeli panah." << endl;
            } else if (senjata == 2) {
                cout << "Anda membeli pedang." << endl;
            } else if (senjata == 3) {
                cout << "Anda membeli catalyst." << endl;
            } else {
                cout << "Pilihan senjata tidak valid." << endl;
                goto Balik3;
            }
        } else {
            cout << "Pilihan tidak valid." << endl;
            goto Balik2;
        }
    } while (health > 0 && healthmusuh > 0);

    #ifdef _WIN32
    	system("CLS");
	#else
    	system("clear");
	#endif

	if (health <= 0 && healthmusuh > 0) {
		kondisiPermainan = 0;
	} else if (healthmusuh <= 0 && health > 0) {
		kondisiPermainan = 1;
	} else if (health <= 0 && healthmusuh <= 0){
		kondisiPermainan = 2;
	}

	if (kondisiPermainan == 0) {
		cout << "GAME OVER\nKamu telah dikalahkan oleh Raja Hytam" << endl;
	} else if (kondisiPermainan == 1) {
    	cout << "MISSION COMPLETE\nRaja Hytam telah di kalahkan dan game selesai." << endl;
    } else if (kondisiPermainan == 2) {
    	cout << "DRAW\nKamu dan Raja Hytam telah mati bersama" << endl;
	}

Balik4:
	cout << "Pilihan Menu" << endl;
    cout << "1. Kembali ke awal" << endl;
    cout << "2. Keluar dari aplikasi" << endl;
    cout << "Pilihan: ";
    cin >> subMenu;

	#ifdef _WIN32
    	system("CLS");
	#else
    	system("clear");
	#endif

	if(subMenu == 1) {
		goto Game;
	} else if (subMenu == 2) {
		cout << "Terima kasih telah Bermain Rajeg Warrior!\n" << endl;
		return 0;
	} else {
		cout << "Pilihan tidak valid." << endl;
        goto Balik4;
	}
}
