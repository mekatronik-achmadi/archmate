#include <iostream>
#include "pwr.h"

int main(int argc, char *argv[])
{
    Pwr *pwr = new Pwr();

    std::cout << std::to_string(pwr->power(4, 3)) << std::endl;

    return 0;
}
