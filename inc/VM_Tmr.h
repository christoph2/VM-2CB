/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
 *                                      cpu12.gems@googlemail.com>
 *
 *   All Rights Reserved
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License along
 *  with this program; if not, write to the Free Software Foundation, Inc.,
 *  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */
#if !defined(__VM_TMR_H)
#define __VM_TMR_H

#include "VM.h"
#include "VM_Cntr.h"

typedef enum tagTimerTickResType {
    TIMER_TICK_RES1,
    TIMER_TICK_RES2,
    TIMER_TICK_RES5,
    TIMER_TICK_RES10,
    TIMER_TICK_RES100
} TimerTickResType;

void    TMR_Init(void);
uint32  TMR_GetTofCount(void);
void    TMR_TimerTick(void);


#if 0
void TimerSetTickRes(TimerTickResType tr);
#endif

#endif  /* __VM_TMR_H */
