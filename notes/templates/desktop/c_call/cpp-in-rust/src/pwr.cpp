#include "pwr.h"

Pwr::Pwr(){}

Pwr::~Pwr(){}

int Pwr::power(int x, int y) {
    int ret = 1;

    for(int i=0;i<y;i++){
        ret = ret * x;
    }

    return ret;
}

