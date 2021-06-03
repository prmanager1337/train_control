// =============================================================================
// Created By  : Anton Sundqvist
// Created Date: 2021-05-11
/* =============================================================================

   =============================================================================*/
// Imports
#include <Wire.h>
#include <math.h>
// =============================================================================
void setup() {
  Serial.begin(115200);
  Wire.begin();
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    int x, address, command_send;
    
    if(Serial.available() > 0){
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      x = Serial.readString().toInt();
      
      //address = floor(x / 100);
      command_send = x % 100;  

      Wire.beginTransmission(2); // transmit to device #4
      Wire.write(command_send); // sends one byte  
      Wire.endTransmission(); // stop transmitting 
      
      digitalWrite(LED_BUILTIN, LOW);
    }
}
