#include <Servo.h>

#define TRIG_PIN 9
#define ECHO_PIN 8
#define SERVO_PIN 3

Servo servo;

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  servo.attach(SERVO_PIN);
  servo.write(0); // posisi awal tertutup
  Serial.begin(9600);
}

void loop() {
  long duration, distance;

  // kirim sinyal trigger
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // baca sinyal echo
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2; // dalam cm

  Serial.print("Jarak: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance <= 20) {
    servo.write(90); // buka tutup
    delay(1500);     // tunggu 3 detik
    servo.write(0);  // tutup kembali
    delay(1000);
  }

  delay(200);
}