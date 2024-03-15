#include "pwr.h"

Pwr::Pwr() {

}

Pwr::~Pwr() {

}

uint16_t Pwr::power(uint8_t x, uint8_t y){
    uint16_t res = 1;

    for (uint8_t i = 0; i<y; i++) {
        res = res * x;
    }

    return res;
}

