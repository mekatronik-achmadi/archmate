#include <Arduino.h>
#include <Arduino_FreeRTOS.h>

void task_blink(void *pvParameter){
    while (1) {
        digitalWrite(13,HIGH);
        vTaskDelay(100/portTICK_PERIOD_MS);
        digitalWrite(13,LOW);
        vTaskDelay(100/portTICK_PERIOD_MS);
    }
}

void task_uart(void *pvParameter){
    while (1) {
        vTaskDelay(100/portTICK_PERIOD_MS);
        Serial.println("Serial OK");
    }
}

void setup(){
    Serial.begin(115200);
    pinMode(13, OUTPUT);

    xTaskCreate(task_blink,
            "led task",
            256,
            NULL,
            tskIDLE_PRIORITY+1,
            NULL);
    xTaskCreate(task_uart,
            "uart task",
            2048,
            NULL,
            tskIDLE_PRIORITY+2,
            NULL);
}

void loop(){}

