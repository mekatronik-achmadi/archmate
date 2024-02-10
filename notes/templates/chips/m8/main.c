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

    while ((UCSRA & (1<<UDRE))==0) {};
    tmp=UDR;

    return tmp;
}

static int uart_putchar(char chr, FILE *stream){
    if(chr=='\n') uart_putchar('\r',stream);

    while ((UCSRA & (1<<UDRE))==0) {};
    UDR=chr;

    return 0;
}

static void uart_init(void){
    DDRD |= 1<<1;

    UCSRB |= 1<<RXEN | 1<< TXEN;
    UCSRB |= 1<<RXCIE;
    UCSRC |= 1<<UCSZ0 | 1<<UCSZ1;

    UBRRH = ((F_CPU/(BAUDRATE*16UL))-1)>>8;
    UBRRL = ((F_CPU/(BAUDRATE*16UL))-1);

    fdev_setup_stream(&uart_in,NULL,uart_getchar,_FDEV_SETUP_READ);
    fdev_setup_stream(&uart_out,uart_putchar,NULL,_FDEV_SETUP_WRITE);

    sei();
}

int main(void)
{
    DDRD |= 1<<3;

    uart_init();
    printf("Setup Done\n");

    while (1) {
       PORTD ^= 1<<3;
       printf("Serial OK\n");
       _delay_ms(500);
    }
    return 0;
}

ISR(USART_RXC_vect){
    scanf("%s",inString);

    if(strcmp(inString,"test")==0){
        printf("Serial OK\n");
    }
    else{
        printf("%s?\n",inString);
    }
}

