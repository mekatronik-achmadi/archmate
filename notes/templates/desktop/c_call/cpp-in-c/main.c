#include <stdio.h>
#include <stdint.h>

#include "pwr_wrap.h"

int main(int argc, char *argv[])
{
    uint16_t res;

    pPwr objPwr = Pwr_new();

    res = Pwr_power(objPwr,4,3);
    printf("Power C from C++: %i\r\n",res);

    Pwr_del(objPwr);

    return 0;
}
