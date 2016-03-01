SUBDIRS = .
vpath %.c ./src
bin_PROGRAMS = vm2cb
vm2cb_SOURCES = Hal.c Hw_Cfg.c Utl.c VM_Al.c VM_Cal.c VM_Can.c\
	VM_Cntr.c VM_Com.c VM_Core.c VM_Excp.c VM_Hm.c\
	VM_Iic.c VM_Lcd.c VM_Lpt.c VM_Ls.c VM_Main.c\
	VM_Math.c VM_Ops.c VM_Plm.c VM_Ports.c VM_Str.c\
	VM_SysMsg.c VM_Tmr.c VM_Twb.c
AM_CFLAGS = -std=c99 -ggdb -gdwarf-2 -I ./inc -Wextra
AM_LDFLAGS = -lm
TESTS = testme.py
