// =============================================================================
// Created By  : Anton Sundqvist
// Created Date: 2021-05-11
/* =============================================================================

   =============================================================================*/
// Imports
#include <Wire.h>
#include <math.h>
// =============================================================================



int i2c_adress, conf = 0;

void setup() {
  pinMode(A3, INPUT); //DIP switch
  pinMode(A2, INPUT); //DIP switch
  pinMode(A1, INPUT); //DIP switch
  pinMode(A0, INPUT); //DIP switch

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

  Serial.begin(115200);
  Wire.begin(1);

}

void loop() {
    int x, address, command_send;
    
    while (!Serial.available());

    x = Serial.readString().toInt();

    Serial.print(conf); //Confirm measeage recived 

    address = floor(x / 100) + 1;
    command_send = x % 100;
    

    Wire.beginTransmission(address); // transmit to device #4
    Wire.write(command_send);              // sends one byte  
    Wire.endTransmission();    // stop transmitting
}
