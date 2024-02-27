#include <avr/io.h>

int main(void)
{
    DDRB |= 1<<5;
    PORTB |= 1<<5;

    return 0;
}
