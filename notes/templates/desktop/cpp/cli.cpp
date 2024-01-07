#include "cli.h"
#include <ostream>

Cli::Cli(){
    strMsg = "C++ Template\r\n";
}

Cli::~Cli(){}

void Cli::Cli_Msg(){
    std::cout << strMsg;
}
