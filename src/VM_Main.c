/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *   (C) 2007-2014 by Christoph Schueler <github.com/Christoph2,
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

#include <WinSock2.h>
#include "VM_Hm.h"

#include "Com_WinSock.h"

/*
    TODO: Endianess als Cfg.-Parameter!
*/

void Vm_Init_Phase0(void);

void Fls_Test(void);

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_MAIN_START_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */

// VHostmode Server Port: 42244.

boolean StartServer(void);
boolean ShutdownServer(void);

int main(void)
{
    CPU_DISABLE_ALL_INTERRUPTS();

    //Fls_Test();

    if (StartServer()) {
        ShutdownServer();
    }
    Vm_Init_Phase0();

    TMR_Init();

    if (Hm_ButtonBootstrapMode()) {

    }  else if (Hm_ButtonHostMode() || VM_BlankCheck()) {
        Hm_Dispatcher();
    }  else {
        VM_SchedInit();
        VM_SysInit();
        CPU_ENABLE_ALL_INTERRUPTS();
        VM_Schedule();
    }

    return 0;
}


void Vm_Init_Phase0(void)
{
    HAL_INIT_PHASE0();
}

static SOCKET so;

boolean StartServer(void)
{

    if (ComWinsock_InitWinsock()) {

        so = ComWinsock_CreateTCPSocket();
        if (!so) {
            return FALSE;
        }

        if (!ComWinsock_ReuseSocket(so)) {
            closesocket(so);
            return FALSE;
        }

        if (!ComWinsock_BindSocket(so, 42244)) {
            return FALSE;
        }

        if (!ComWinsock_ListenSocket(so, 1)) {
            return FALSE;
        }

        if (!ComWinsock_AcceptSocket(so)) {
            return FALSE;
        }

        return TRUE;
    } else {
        return FALSE;
    }
}

boolean ShutdownServer(void)
{
    ComWinsock_DeinitWinsock();
    closesocket(so);
}

#if VM_MEMORY_MAPPING == STD_ON
    #define VM_MAIN_STOP_SEC_CODE
    #include "MemMap.h"
#endif /* VM_MEMORY_MAPPING */
