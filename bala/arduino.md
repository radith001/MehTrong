## 1. Library dan Inisialisasi

```cpp
#include <Servo.h>
#define TRIG_PIN 9
#define ECHO_PIN 8
#define SERVO_PIN 3

Servo servo;
```

- `Servo.h` adalah library untuk mengontrol motor servo.
- Pin `TRIG_PIN` dan `ECHO_PIN` digunakan untuk sensor HC-SR04.
- Servo dihubungkan ke pin D3.

## 2. Setup

```cpp
void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  servo.attach(SERVO_PIN);
  servo.write(0); // posisi awal tertutup
  Serial.begin(9600);
}
```

- Mengatur mode pin: `TRIG_PIN` sebagai OUTPUT dan `ECHO_PIN` sebagai INPUT.
- Servo dipasang dan diarahkan ke posisi tertutup (0 derajat).
- Komunikasi serial diaktifkan untuk menampilkan hasil pengukuran jarak ke Serial Monitor.

## 3. Loop Utama

### a. Deklarasi Variabel

```cpp
long duration, distance;
```

- `duration` menyimpan waktu pantulan ultrasonik.
- `distance` menyimpan hasil konversi waktu menjadi jarak dalam sentimeter.

### b. Mengirim Sinyal Ultrasonik

```cpp
digitalWrite(TRIG_PIN, LOW);
delayMicroseconds(2);
digitalWrite(TRIG_PIN, HIGH);
delayMicroseconds(10);
digitalWrite(TRIG_PIN, LOW);
```

- Menghasilkan sinyal trigger ultrasonik selama 10 mikrodetik untuk memulai pengukuran jarak.

### c. Membaca Jarak

```cpp
duration = pulseIn(ECHO_PIN, HIGH);
distance = duration * 0.034 / 2;
```

- `pulseIn(ECHO_PIN, HIGH)` mengukur durasi pantulan sinyal yang diterima oleh pin Echo.
- Menghitung jarak berdasarkan durasi pantulan dengan rumus `distance = duration * 0.034 / 2`, di mana 0.034 cm/µs adalah kecepatan suara.

### d. Menampilkan Jarak

```cpp
Serial.print("Jarak: ");
Serial.print(distance);
Serial.println(" cm");
```

- Mencetak hasil pengukuran jarak ke Serial Monitor agar kita bisa melihat jarak antara sensor dan objek.

### e. Logika Servo Otomatis

```cpp
if (distance <= 15) {
  servo.write(90); // buka
  delay(3000);     // tunggu 3 detik
  servo.write(0);  // tutup
  delay(1000);
}
```

- Jika objek terdeteksi dalam jarak kurang dari atau sama dengan 15 cm, servo bergerak ke posisi 90° (membuka).
- Menunggu selama 3 detik untuk memberi waktu servo terbuka.
- Setelah itu, servo kembali ke posisi 0° (menutup).
- Ada delay tambahan 1 detik sebelum pengulangan selanjutnya.


