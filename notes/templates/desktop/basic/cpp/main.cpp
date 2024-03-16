#include "cli.h"

int main(int argc, char *argv[])
{
    Cli *cli = new Cli();
    cli->Cli_Msg();

    delete cli;

    return 0;
}
