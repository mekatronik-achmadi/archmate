#include "pwr.h"

namespace org {
namespace pwr {

Pwr::Pwr() {}

Pwr::~Pwr() {}

unsigned int Pwr::power(unsigned int x, unsigned int y){
    unsigned int res = 1, i = 0;

    while (i<y) {
        res = res * x;
        i = i + 1;
    }

    return res;
}

}}

