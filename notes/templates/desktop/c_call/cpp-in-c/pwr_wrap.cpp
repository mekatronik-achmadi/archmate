#include "pwr_wrap.h"

pPwr Pwr_new(){
    return new Pwr();
}

void Pwr_del(pPwr self){
    delete reinterpret_cast<Pwr*>(self);
}

uint16_t Pwr_power(pPwr self, uint8_t x, uint8_t y){
    auto p = reinterpret_cast<Pwr*>(self);
    return p->power(x,y);
}

