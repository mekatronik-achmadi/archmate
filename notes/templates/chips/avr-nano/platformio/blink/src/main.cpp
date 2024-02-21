#include <Arduino.h>

void setup(){
    Serial.begin(115200);
    pinMode(13, OUTPUT);
}

void loop(){
    digitalWrite(13,HIGH);
    delay(200);
    digitalWrite(13,LOW);
    delay(200);

    Serial.println("Serial OK");
}

