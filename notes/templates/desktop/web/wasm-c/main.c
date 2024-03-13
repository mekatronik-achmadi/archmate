#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include "pwr.h"

int main(int argc, char *argv[])
{
    printf("WASM from C\r\n");
    printf("result: %i\r\n",calc_pwr(4, 3));

    return 0;
}
