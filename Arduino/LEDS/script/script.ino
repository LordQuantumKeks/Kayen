void setup() {
  pinMode(7, OUTPUT);
}

void loop() {
  digitalWrite(7, HIGH);
  delay(10000);
  digitalWrite(7, LOW);
  delay(10000);  
}
