void setup() {
 
   pinMode(4,OUTPUT);
   Serial.begin(9600);
   Serial.println("Reading From the Sensor ...");
   delay(2000);
}

  void loop() {
  digitalWrite(4, HIGH);
  delay(2000);
  digitalWrite(4, LOW);
  delay(2000);
}
