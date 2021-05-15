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
  
  Wire.begin(set_adress);

  Wire.onReceive(receiveEvent);

}

//Sets the i2c adress of the decive based on the state of the DIP switch
int set_adress() {

  int adress = 0;

  if(digitalRead(A0) == 1){
    bitSet(adress, 0);
  }
  if(digitalRead(A1) == 1){
    bitSet(adress, 1);
  }
  if(digitalRead(A2) == 1){
    bitSet(adress, 2);
  }
  if(digitalRead(A3) == 1){
    bitSet(adress, 3);
  }

  return adress;
}

void receiveEvent(int howMany) {
  
  int switch_number, switch_setting, number_array[7] = { -1, 0, 1, 2, 3, 4, 5 }; //Array for calulating the correct pin to toggle for switches in the state of 1

  while (Wire.available()) { // loop through all but the last
    int switch_command = Wire.read(); // receive byte as a character

    int toggle = 0; //Initelize the toggle of the switch
    switch_number = switch_command  / 10;
    switch_setting = switch_command  % 10;

    if(switch_setting == 1){
        toggle = switch_number + number_array[switch_number - 1];
        digitalWrite(toggle, HIGH);
    }
    else if(switch_setting == 2){ 
        toggle = switch_number * 2 - 1;
        digitalWrite(toggle, HIGH);
    }
    delay(500);
    digitalWrite(toggle, LOW);
  }
}

void loop() {
  if(i2c_adress == 1){
    while (!Serial.available());

    x = Serial.readString().toInt();
    int toggle = 0;
    switch_number = x / 10;
    switch_setting = x % 10;

    if(switch_setting == 1){
      toggle = switch_number * 2 - 1;
      digitalWrite(toggle, HIGH);
    }
    else if(switch_setting == 2){
      toggle = switch_number * 2;
      digitalWrite(toggle, HIGH);
    }
    Serial.print(conf); //Confirm measeage recived  
    delay(1000);
    digitalWrite(toggle, LOW);
  }
  else{
    delay(100);
  }

}
