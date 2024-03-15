#include <iostream>

#include "cli.h"
#include "pwr.h"

Cli::Cli(){
    v_x = 4;
    v_y = 3;
}

Cli::~Cli(){}

void Cli::Cli_Msg(){
    std::cout
        << "Power C++ from C: "
        << std::to_string(calc_pwr(v_x,v_y))
        << std::endl;
}
