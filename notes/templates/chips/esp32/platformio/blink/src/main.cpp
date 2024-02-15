#include <Arduino.h>

#define LED_BUILTIN GPIO_NUM_2

void setup(){
    Serial.begin(115200);
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop(){
    digitalWrite(LED_BUILTIN,HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN,LOW);
    delay(200);

    Serial.println("Serial ESP32");
}

