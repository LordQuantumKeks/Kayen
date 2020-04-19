void setup() {
 
   pinMode(7,OUTPUT);
   Serial.begin(9600);
   Serial.println("Reading From the Sensor ...");
   delay(2000);
}

  void loop() {
  digitalWrite(7, HIGH);
  Serial.println("on");
  delay(5000);
  digitalWrite(7, LOW);
  Serial.println("off");
  delay(5000);
}
