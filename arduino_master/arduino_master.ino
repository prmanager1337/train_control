String x;
int i = 1;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString();
  if(x == "1"){
    digitalWrite(LED_BUILTIN, HIGH);
  }
  Serial.print(i);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  
}
