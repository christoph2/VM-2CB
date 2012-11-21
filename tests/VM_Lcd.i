
%module vm_lcd

%include "Types.i"

%{
#include "VM.h"

void Lcd_init(void), Lcd_show_cursor(void), Lcd_clear(void);
void Lcd_clreol(void), Lcd_goto(void), Lcd_home(void);
void Lcd_scroll(void), Lcd_ready(void), Lcd_put(void), Lcd_print(void);

%}

void Lcd_init(void), Lcd_show_cursor(void), Lcd_clear(void);
void Lcd_clreol(void), Lcd_goto(void), Lcd_home(void);
void Lcd_scroll(void), Lcd_ready(void), Lcd_put(void), Lcd_print(void);

