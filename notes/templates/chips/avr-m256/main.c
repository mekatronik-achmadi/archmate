#include <avr/io.h>

#include <FreeRTOS.h>
#include <task.h>

static void ledTask(void *pvParameter){
    while (1) {
        PORTB ^= 1<<5;
        vTaskDelay(200/portTICK_PERIOD_MS);
    }
}

int main(void){
    DDRB |= 1<<5;
    PORTB |= 1<<5;

    xTaskCreate(&ledTask,
    "BLink",
    256,
    NULL,
    1,
    NULL);

    return 0;
}
