#include <Servo.h>

Servo horizontalServo;  // Horizontal servo
Servo verticalServo;    // Vertical servo

void setup() {
  // Attach servos to pins
  horizontalServo.attach(9);
  verticalServo.attach(10);

  // Initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the angles from serial
    int horizontalAngle = Serial.parseInt();
    int verticalAngle = Serial.parseInt();

    // Move the servos to the specified angles
    horizontalServo.write(horizontalAngle);
    verticalServo.write(verticalAngle);
  }
}
