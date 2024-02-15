#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CHARLEN     16
#define BAUDRATE    9600

char inString[CHARLEN];

FILE uart_in = {0};
FILE uart_out = {0};

static int uart_getchar(FILE *stream){
    (void) stream;
    char tmp;

    while ((UCSR0A & (1<<RXC0))==0) {};
    tmp=UDR0;

    return tmp;
}

static int uart_putchar(char chr, FILE *stream){
    if(chr=='\n') uart_putchar('\r',stream);

    while ((UCSR0A & (1<<UDRE0))==0) {};
    UDR0=chr;

    return 0;
}

static void uart_init(void){
    DDRD |= 1<<1;

    UCSR0B |= 1<<RXEN0 | 1<< TXEN0;
    UCSR0B |= 1<<RXCIE0;
    UCSR0C |= 1<<UCSZ00 | 1<<UCSZ01;

    UBRR0H = ((F_CPU/(BAUDRATE*16UL))-1)>>8;
    UBRR0L = ((F_CPU/(BAUDRATE*16UL))-1);

    fdev_setup_stream(&uart_in,NULL,uart_getchar,_FDEV_SETUP_READ);
    stdin = &uart_in;

    fdev_setup_stream(&uart_out,uart_putchar,NULL,_FDEV_SETUP_WRITE);
    stdout = &uart_out;

    sei();
}

int main(void)
{
    DDRB |= 1<<5; // Arduino: D13

    uart_init();
    printf("Setup Done\n");

    while (1) {
       PORTB ^= 1<<5;
       _delay_ms(200);
    }
    return 0;
}

ISR(USART_RX_vect){
    scanf("%s",inString);

    if(strcmp(inString,"test")==0) printf("Serial OK\n");
    else printf("%s?\n",inString);

    return;
}

