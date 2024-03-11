#include <stdio.h>
#include "msg.h"

static char strMsg[32];

void init_msg(void){
    sprintf(strMsg,"%s","C in C++ Template");
}

void print_msg(void){
    printf("%s\r\n",strMsg);
}
