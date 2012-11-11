/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *  (C) 2007-2012 by Christoph Schueler <chris@konnex-tools.de,
 *                                       cpu12.gems@googlemail.com>
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
#if !defined(__ISR_CFG_H)
#define __ISR_CFG_H

DECLARE_ISR1_VECTOR(ATD0_Vector);
#define ATD0_VECTOR     ATD0_Vector

DECLARE_ISR1_VECTOR(SystemTimerHandler);
#define MDCU_VECTOR     SystemTimerHandler

DECLARE_ISR1_VECTOR(TMR_TofHandler);
#define TOF_VECTOR      TMR_TofHandler

#if 0
DECLARE_ISR1_VECTOR(RTI_Vector);
#define RTI_VECTOR      RTI_Vector
#endif

DECLARE_ISR1_VECTOR(SCI0_Vector);
#define SCI0_VECTOR     SCI0_Vector

DECLARE_ISR1_VECTOR(SCI1_Vector);
#define SCI1_VECTOR     SCI1_Vector

#if 0
DECLARE_ISR1_VECTOR(iic_handler);
#define IIC_VECTOR      iic_handler
#endif

DECLARE_ISR1_VECTOR(PAOVIHandler);
#define PAOF_VECTOR     PAOVIHandler

DECLARE_ISR1_VECTOR(PBOVIHandler);
#define PBOF_VECTOR     PBOVIHandler

DECLARE_ISR1_VECTOR(PORTHHandler);
#define PH_VECTOR       PORTHHandler

DECLARE_ISR1_VECTOR(SPI0_Vector);
#define SPI0_VECTOR     SPI0_Vector

#if 0
DECLARE_ISR1_VECTOR(CAN0TxVector);
#define CAN0T_VECTOR    CAN0TxVector

DECLARE_ISR1_VECTOR(CAN0RxVector);
#define CAN0R_VECTOR    CAN0RxVector

DECLARE_ISR1_VECTOR(CAN0ErrorVector);
#define CAN0E_VECTOR    CAN0ErrorVector

DECLARE_ISR1_VECTOR(CAN0WakupVector);
#define CAN0W_VECTOR    CAN0WakupVector
#endif

#endif /* __ISR_CFG_H */

