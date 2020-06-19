#include <dht.h>

#include <FirmataMarshaller.h>
#include <Firmata.h>
#include <FirmataParser.h>
#include <FirmataDefines.h>
#include <FirmataConstants.h>
#include <Boards.h>

#include <dht.h>

dht DHT;

//Definition des Digial Pins für den Temp sensor
#define DHT11_PIN 6

void setup() {
  Serial.begin(9600);
  pinMode(7, OUTPUT);
}

void loop() {
  tempmeasures();
  Serial.print(tempmeasures());
  //Lampenzyklus
  digitalWrite(7, HIGH);
  delay(1000);
  digitalWrite(7, LOW);
  delay(1000);
}

double tempmeasures() {
  int chk = DHT.read11(DHT11_PIN);
  //Serial.print(DHT.humidity);
  //Serial.print(" ");
  //Serial.print(DHT.temperature);
  //Serial.println();
  double x = DHT.temperature;
  //Serial.print(x);
  //Serial.println();
  return x;
}
