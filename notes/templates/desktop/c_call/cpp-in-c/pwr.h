#ifndef PWR_H
#define PWR_H

#include <cstdint>

class Pwr {
    public:
        Pwr();
        ~Pwr();
        uint16_t power(uint8_t x, uint8_t y);
};

#endif
