// =============================================================================
// Created By  : Anton Sundqvist
// Created Date: 2021-05-11
/* =============================================================================

   =============================================================================*/
// Imports
#include <Wire.h>
// =============================================================================



int i2c_adress;

void setup() {
  pinMode(A5, OUTPUT); //I2C Communication Pin
  pinMode(A4, OUTPUT); //I2C Communication Pin

  pinMode(13, OUTPUT); //Train switch control
  pinMode(12, OUTPUT); //Train switch control
  pinMode(11, OUTPUT); //Train switch control
  pinMode(10, OUTPUT); //Train switch control
  pinMode(9, OUTPUT); //Train switch control
  pinMode(8, OUTPUT); //Train switch control
  pinMode(7, OUTPUT); //Train switch control
  pinMode(6, OUTPUT); //Train switch control
  pinMode(5, OUTPUT); //Train switch control
  pinMode(4, OUTPUT); //Train switch control
  pinMode(3, OUTPUT); //Train switch control
  pinMode(2, OUTPUT); //Train switch control
  pinMode(1, OUTPUT); //Train switch control
  pinMode(0, OUTPUT); //Train switch control
  
  Wire.begin(2);

  Wire.onReceive(receiveEvent);

}

//Sets the i2c adress of the decive based on the state of the DIP switch

void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    int switch_command = Wire.read(); // receive byte as a character
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
  }
}

void loop() {
  delay(100);

  digitalWrite(10, HIGH);
  delay(1000);
  digitalWrite(10, LOW);
  delay(1000);
}
