#include <dht.h>

dht DHT;

//Digital Pin definition for Sensor
#define DHT11_PIN 7

void setup(){
  Serial.begin(9600);
}


void loop()
{
  ////////////////// ------ Temperature and Humidity ------ ////////////////
  int chk = DHT.read11(DHT11_PIN);
  Serial.print(DHT.humidity);
  Serial.print(" ");
  Serial.print(DHT.temperature);
  Serial.println();
  delay(5000);
}
