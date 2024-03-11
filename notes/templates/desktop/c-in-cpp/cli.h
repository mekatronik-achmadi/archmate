#ifndef CLI_H
#define CLI_H

#include <cstdint>

class Cli
{
private:
    uint8_t v_x;
    uint8_t v_y;

public:
    Cli();
    virtual ~Cli();
    void Cli_Msg();
};

#endif /* CLI_H */
