#include <avr/io.h>

#include "FreeRTOS.h"
#include "task.h"

void taskBlink(void *pvParams){
    while (1) {
        PORTB ^= 1<<5;
        vTaskDelay(200/portTICK_PERIOD_MS);
    }
}

int main(void)
{

    DDRB |= 1<<5;
    PORTB |= 1<<5;

    xTaskCreate(taskBlink,
            "Blink",
            configMINIMAL_STACK_SIZE,
            NULL,
            tskIDLE_PRIORITY+1,
            NULL);

    vTaskStartScheduler();

    while (1) {
       vTaskDelay(200/portTICK_PERIOD_MS);
    }

    return 0;
}

