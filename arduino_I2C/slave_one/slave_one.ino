// Wire Slave Receiver
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Receives data as an I2C/TWI slave device
// Refer to the "Wire Master Writer" example for use with this

// Created 29 March 2006

// This example code is in the public domain.


#include <Wire.h>

void setup()
{
  pinMode(10, OUTPUT);
  Wire.begin(1);                // join i2c bus with address #1
  Wire.onReceive(receiveEvent); // register event
}

void loop()
{
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{

  int x = Wire.read();
  
  if(x == 1){
      digitalWrite(10, HIGH);
      delay(1000);
  }
  else if(x == 2){
      digitalWrite(10, LOW);
      delay(1000);
  }
}
