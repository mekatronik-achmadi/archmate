#ifndef PWR_WRAP_H
#define PWR_WRAP_H

#ifdef __cplusplus
    #define EXPORT_C extern "C"
#else
    #define EXPORT_C
#endif

#include <stdint.h>

#ifdef __cplusplus

#include <cstdint>

class Pwr {
    public:
        Pwr();
        ~Pwr();
        uint16_t power(uint8_t x, uint8_t y);
};

#endif

typedef void* pPwr ;

EXPORT_C pPwr Pwr_new();
EXPORT_C void Pwr_del(pPwr self);
EXPORT_C uint16_t Pwr_power(pPwr self, uint8_t x, uint8_t y);

#endif
