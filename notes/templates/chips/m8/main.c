#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    DDRC |= 1<<6;
    while (1) {
       PORTC ^= 1<<6;
       _delay_ms(500);
    }
    return 0;
}
