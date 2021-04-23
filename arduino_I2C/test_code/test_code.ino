#include <Wire.h>
int x, conf = 0, switch_number, switch_setting;


void setup() {
  Wire.begin();
  Serial.begin(115200);
  Serial.setTimeout(1);

  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  
  digitalWrite(7, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(5, HIGH);
  digitalWrite(4, HIGH);
  delay(1000);
  digitalWrite(7, LOW);
  digitalWrite(6, LOW);
  digitalWrite(5, LOW);
  digitalWrite(4, LOW);
  
}

void loop() {
  
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
