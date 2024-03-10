#include <ets_sys.h>
#include <osapi.h>
#include <user_interface.h>
#include <os_type.h>
#include <gpio.h>
#include <driver/gpio16.h>
#include "user_config.h"

#define BAUDRATE 115200

static os_timer_t ledTimer;
static uint8_t ledOn = 0;
static void ledTask(void *prv){
    if(ledOn){
        gpio_output_set(0, (1 << 2), 0, 0);
        gpio16_output_set(1);
        ledOn = 0;
    }
    else{
        gpio_output_set((1 << 2), 0, 0, 0);
        gpio16_output_set(0);
        ledOn = 1;
    }
}

static os_timer_t serialTimer;
static void serialTask(void *prv){
    os_printf("Serial OK\n");
}

void user_init(void){
    uart_init(BAUDRATE,BAUDRATE);

    gpio_init();
    gpio16_output_conf();
    gpio_output_set(0, 0, (1 << 2), 0);

    os_timer_setfn(&ledTimer,(os_timer_func_t*) ledTask,NULL);
    os_timer_setfn(&serialTimer,(os_timer_func_t*) serialTask,NULL);

    os_timer_arm(&ledTimer,100,1);
    os_timer_arm(&serialTimer,500,1);
}

