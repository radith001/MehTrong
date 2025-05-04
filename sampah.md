# 🎥 Script Video Penjelasan: Tong Sampah Otomatis

## 👥 Kelompok: Umam, Dini, Radith, Satria

---

## 🎙️ Umam – Pembukaan & Konsep Umum

> **Assalamualaikum warahmatullahi wabarakatuh.**  
> Halo semuanya! Kami dari kelompok [nama kelompok/kelas] ingin mempresentasikan proyek IoT sederhana kami yang berjudul **"Tong Sampah Otomatis"**.  
>  
> Tujuan dari proyek ini adalah untuk mempermudah masyarakat dalam membuang sampah tanpa harus menyentuh tutup tong secara langsung.  
>  
> Dengan bantuan sensor ultrasonik dan servo motor, alat ini akan membuka tutup tong ketika tangan mendekat, lalu otomatis menutup setelah beberapa detik.  
>  
> Untuk lebih jelasnya, penjelasan selanjutnya akan disampaikan oleh Dini.

---

## 🎙️ Dini – Penjelasan Komponen & Rangkaian

> Saya Dini, akan menjelaskan bagian **komponen dan rangkaian** dari alat ini.  
>  
> Pada proyek ini, kami menggunakan simulasi di **Wokwi**, dan komponen utama yang digunakan adalah:
>
> - **Sensor Ultrasonik HC-SR04** untuk mendeteksi jarak.
> - **Servo Motor SG90** untuk membuka dan menutup tutup tong.
> - **Arduino UNO** sebagai mikrokontroler pusat.
> - **Breadboard dan kabel jumper** untuk menghubungkan semua komponen.
>  
> Rangkaian alat dapat dilihat pada gambar simulasi:
>
> - Pin **Trig** dihubungkan ke **D9** pada Arduino.
> - Pin **Echo** ke **D8**.
> - Kabel sinyal servo ke **D3**.
> - VCC sensor dan servo ke **5V Arduino**, dan GND ke **GND**.
>  
> Berikutnya, Radith akan menjelaskan cara kerja programnya.

---

## 🎙️ Radith – Penjelasan Kode Program

> Saya Radith, akan menjelaskan kode program Arduino yang digunakan pada proyek ini.  
>  
> Di awal program, kita gunakan `#include <Servo.h>` untuk mengatur servo motor.  
> Selanjutnya, kita definisikan pin untuk sensor dan servo:
>
> ```cpp
> #define TRIG_PIN 9
> #define ECHO_PIN 8
> #define SERVO_PIN 3
> ```
>
> Pada fungsi `setup()`, kita inisialisasi:
>
> - Trig sebagai OUTPUT
> - Echo sebagai INPUT
> - Servo ke posisi awal tertutup
> - Serial monitor untuk menampilkan jarak
>
> Di dalam fungsi `loop()`, sensor akan mengirim sinyal ultrasonik dan menghitung waktu pantulan:
>
> ```cpp
> distance = duration * 0.034 / 2;
> ```
>
> Jika jarak kurang dari atau sama dengan 15 cm, servo akan membuka selama 3 detik, lalu menutup kembali.  
> Program terus diulang setiap 200 milidetik.

---

## 🎙️ Satria – Simulasi, Manfaat & Penutup

> Saya Satria, akan menunjukkan **cara kerja simulasi** dan menyampaikan manfaat dari alat ini.  
>  
> Saat simulasi dijalankan, kita bisa lihat bahwa ketika ada objek mendekat sensor, servo bergerak membuka.  
> Setelah 3 detik, servo otomatis menutup kembali.  
>  
> Manfaat utama dari alat ini adalah mengurangi kontak tangan dengan tempat sampah, sehingga lebih **higienis dan praktis**.  
>  
> Alat ini bisa dikembangkan lagi, misalnya dengan fitur deteksi penuh, LED indikator, atau notifikasi ke smartphone.  
>  
> Terima kasih atas perhatian dan waktunya.  
> **Wassalamualaikum warahmatullahi wabarakatuh.**

---
