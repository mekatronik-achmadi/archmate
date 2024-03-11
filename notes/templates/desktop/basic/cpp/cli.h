#ifndef CLI_H
#define CLI_H

#include <iostream>
#include <string>

class Cli
{
private:
    std::string strMsg;

public:
    Cli();
    virtual ~Cli();
    void Cli_Msg();
};

#endif /* CLI_H */
