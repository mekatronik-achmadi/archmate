#include <Arduino.h>

#define BLINK_LED 16

void setup(){
    Serial.begin(115200);
    pinMode(BLINK_LED,OUTPUT);
}

void loop(){
    digitalWrite(BLINK_LED, HIGH);
    delay(200);
    digitalWrite(BLINK_LED, LOW);
    delay(200);

    Serial.println("Serial OK");
}
