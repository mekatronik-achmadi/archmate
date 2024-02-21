#include <Arduino.h>
#include <Arduino_FreeRTOS.h>

void blink_task(void* pvParameter){
    (void) pvParameter;

    while (1) {
        digitalWrite(13,HIGH);
        vTaskDelay(100/portTICK_PERIOD_MS);
        digitalWrite(13,LOW);
        vTaskDelay(100/portTICK_PERIOD_MS);
    }
}

void setup(){

    Serial.begin(9600);
    pinMode(13, OUTPUT);

    xTaskCreate(blink_task,
            "Blink",
            128,
            NULL,
            tskIDLE_PRIORITY+1,
            NULL);
}

void loop(){
    Serial.println("Serial OK");
    vTaskDelay(100/portTICK_PERIOD_MS);
}

