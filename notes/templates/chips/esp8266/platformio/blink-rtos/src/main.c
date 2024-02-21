#include <esp_common.h>
#include <freertos/task.h>
#include <gpio.h>
#include <uart.h>

uint32 user_rf_cal_sector_set(void)
{
    flash_size_map size_map = system_get_flash_size_map();
    uint32 rf_cal_sec = 0;
    switch (size_map) {
        case FLASH_SIZE_4M_MAP_256_256:
            rf_cal_sec = 128 - 5;
            break;

        case FLASH_SIZE_8M_MAP_512_512:
            rf_cal_sec = 256 - 5;
            break;

        case FLASH_SIZE_16M_MAP_512_512:
        case FLASH_SIZE_16M_MAP_1024_1024:
            rf_cal_sec = 512 - 5;
            break;

        case FLASH_SIZE_32M_MAP_512_512:
        case FLASH_SIZE_32M_MAP_1024_1024:
            rf_cal_sec = 1024 - 5;
            break;

        default:
            rf_cal_sec = 0;
            break;
    }

    return rf_cal_sec;
}

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
