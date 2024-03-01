#include <esp_common.h>
#include <freertos/task.h>
#include <gpio.h>
#include <uart.h>

static void task_blink(void* ignore){
    while (1) {
        gpio16_output_set(0);
        vTaskDelay(100/portTICK_RATE_MS);

        gpio16_output_set(1);
        vTaskDelay(100/portTICK_RATE_MS);
    }
}

static void task_uart(void* ignore){
    while (1) {
        os_printf("Serial OK\r\n");
        vTaskDelay(100/portTICK_RATE_MS);
    }
}

void user_init(void){
    gpio16_output_conf();

    uart_init_new();
    UART_SetBaudrate(UART0,BIT_RATE_115200);

    xTaskCreate(&task_blink,"blink_led",256,NULL,tskIDLE_PRIORITY+1,NULL);
    xTaskCreate(&task_uart,"uart_send",1024,NULL,tskIDLE_PRIORITY+2,NULL);

}
