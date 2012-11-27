/*
 *   2-CB (C-Control-II kompatible Virtuelle Maschine).
 *
 *  (C) 2007-2012 by Christoph Schueler <github.com/Christoph2,
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

#include "hal/windows/Win_FlsEmu.h"
#include "VM_Cfg.h"
#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <Windows.h>


/*
**
**  Hinweis: Auch wenn der Flash-Emulator funktionert so wie so soll, ist die gegenwärtige Lösung suboptimal,
**           weil allgemeine Konzepte mit HC12 Spezifika vermischt werden...
**
*/

/*
**  TODO: C++ !!!
*/

#define KB(v)   ((v) * 0x400)
#define MB(v)   ((v) * (0x400 * 0x400))

#define FILL_CHAR   0xff

#define TOP_PAGE    0x3f

// lowpage = TOP_PAGE - (totalSize / pageSize) + 1;

typedef struct tagFileViewType {
    HANDLE mappingHandle;
    void * mappingAddress;
} FileViewType;


typedef struct tagPersistentArrayType {
    HANDLE fileHandle;
    HANDLE mappingHandle;
    void * mappingAddress;
    unsigned __int16 currentPage;
} PersistentArrayType;


typedef enum tagOpenCreateType {
    OPEN_ERROR,
    OPEN_EXSISTING,
    NEW_FILE
} OpenCreateType;


typedef struct tagFlsEmu_Traits {
    wchar_t          name[32];
    unsigned __int32 memSize;
    unsigned __int8  writeSize;
    unsigned __int16 sectorSize;
    unsigned __int32 pageSize;
    unsigned __int8 blockCount;
    unsigned __int8 erasedValue;
    unsigned __int32 cycles;
    PersistentArrayType * persistentArray;
} FlsEmu_Traits;

/*
**  Lokale Variablen.
*/
static DWORD pageSize;
static DWORD allocationGranularity;

void printErrorMessage(wchar_t const * func, DWORD error);
/*
**  Lokale Funktions-Prototypen.
*/
static void MemoryInfo(void * address);
static HANDLE OpenCreateFile(wchar_t const * fileName, BOOL create);
static BOOL CreateFileView(HANDLE handle, DWORD length, FileViewType * fileView);
static void CloseFileView(FileViewType * fileView);
static OpenCreateType CreatePersitentArray(wchar_t const * fileName, DWORD size, PersistentArrayType * persistentArray);
static void ClosePersitentArray(PersistentArrayType const * persistentArray);

static FlsEmu_Traits S12D512FlashArray = {
    L"VM2CB_Flash",
    KB(512),
    2,
    FLS_SECTOR_SIZE,
    FLS_PAGE_SIZE,
    4,
    0xff,
    10,
};
// sort of complicated for an embedded systems guy..

static FlsEmu_Traits S12D512EEPROMArray = {
    L"VM2CB_EEPROM",
    KB(4),
    2,
    4,
    KB(4),
    1,
    0xff,
    10000
};


/*
**  Lokale Funktionen.
*/
static void MemoryInfo(void * address)
{
    MEMORY_BASIC_INFORMATION info;

    VirtualQuery(address, &info, sizeof(MEMORY_BASIC_INFORMATION));
}


static HANDLE OpenCreateFile(wchar_t const * fileName, BOOL create)
{
    HANDLE handle;

    if (create == FALSE) {
        handle = CreateFile((LPCWSTR)fileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, 
            (LPSECURITY_ATTRIBUTES)NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL | FILE_FLAG_RANDOM_ACCESS, (HANDLE)NULL
        );  
    } else {
        handle = CreateFile((LPCWSTR)fileName, GENERIC_READ | GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, 
            (LPSECURITY_ATTRIBUTES)NULL, CREATE_NEW, FILE_ATTRIBUTE_NORMAL | FILE_FLAG_RANDOM_ACCESS, (HANDLE)NULL
        );
    }

    //GetFileNameFromHandle(handle);

    return handle;
}

static BOOL CreateFileView(HANDLE handle, DWORD length, FileViewType * fileView)
{
    fileView->mappingHandle = CreateFileMapping(handle, (LPSECURITY_ATTRIBUTES)NULL, PAGE_READWRITE, (DWORD)0, (DWORD)length, NULL);
    if (fileView->mappingHandle == NULL) {     
        return FALSE;
    }

    /* TODO: Refactor to function; s. FlsEmu_MapView() */
    fileView->mappingAddress = (void *)MapViewOfFile(fileView->mappingHandle, FILE_MAP_ALL_ACCESS, 0, 0, length);
    if (fileView->mappingAddress == NULL) {
        CloseHandle(fileView->mappingHandle);
        return FALSE;
    }

    return TRUE;
}

static void CloseFileView(FileViewType * fileView)
{
    CloseHandle(fileView->mappingHandle);
}

static OpenCreateType CreatePersitentArray(wchar_t const * fileName, DWORD size, PersistentArrayType * persistentArray)
{
    DWORD error;
    FileViewType fileView;
    OpenCreateType result;
    boolean newFile = FALSE;

    persistentArray->fileHandle = OpenCreateFile(fileName, FALSE);
    if (persistentArray->fileHandle == INVALID_HANDLE_VALUE) {
        error = GetLastError();
        if (error == ERROR_FILE_NOT_FOUND) {
            newFile = TRUE;
            persistentArray->fileHandle = OpenCreateFile(fileName, TRUE);
            if (persistentArray->fileHandle == INVALID_HANDLE_VALUE) {
                return OPEN_ERROR;
            }
        } else {
            return OPEN_ERROR;
        }
    }

    if (!CreateFileView(persistentArray->fileHandle, size, &fileView)) {
        return OPEN_ERROR;
    }

    persistentArray->mappingAddress = fileView.mappingAddress;
    persistentArray->mappingHandle  = fileView.mappingHandle;

    MemoryInfo(persistentArray->mappingAddress);

    if (newFile) {
        result = NEW_FILE;
    } else {
        result = OPEN_EXSISTING;
    }
    return result;
}

static void ClosePersitentArray(PersistentArrayType const * persistentArray)
{
    UnmapViewOfFile(persistentArray->mappingAddress);
    CloseHandle(persistentArray->mappingHandle);
    CloseHandle(persistentArray->fileHandle);
}

void * FlsEmu_BasePointer(FlsEmu_Traits * traits)
{
    return traits->persistentArray->mappingAddress;
}

void FlsEmu_Create(FlsEmu_Traits * traits)
{
    int pos;
    DWORD error;
    wchar_t * pdest;
    wchar_t adm[128];
    PersistentArrayType temp;
    OpenCreateType result;

    traits->persistentArray = (PersistentArrayType *)malloc(sizeof(PersistentArrayType));

    pdest = wcschr(traits->name, L'.');
    if (pdest != NULL) {
        pos = (pdest - traits->name + 1);

        wcsncpy_s((wchar_t *)adm, _countof(adm), (wchar_t *)traits->name, pos);
        wcscat_s(adm, _countof(adm), L"adm");
    } else {
        wcsncpy_s((wchar_t *)adm, _countof(adm), (wchar_t *)traits->name, lstrlen(traits->name));
        wcscat_s(adm, _countof(adm), L".adm");
        wcscat_s((wchar_t *)traits->name, _countof(traits->name), L".rom");                
    }
 
    result = CreatePersitentArray(traits->name, traits->memSize, traits->persistentArray);
    if (result == OPEN_ERROR) {
        error = GetLastError();
        printErrorMessage(L"CreatePersitentArray", error);
    } else if (result == NEW_FILE) {
        FillMemory(traits->persistentArray->mappingAddress, traits->memSize, traits->erasedValue);
    }

    result = CreatePersitentArray(adm, sizeof(FlsEmu_Traits) + (traits->memSize * sizeof(unsigned __int32)), &temp);
    if (result == OPEN_ERROR) {
        error = GetLastError();
        printErrorMessage(L"CreatePersitentArray", error);
    } else if (result == NEW_FILE) {
        memcpy(temp.mappingAddress, traits, sizeof(FlsEmu_Traits));
        ZeroMemory((unsigned __int8 *)temp.mappingAddress + sizeof(FlsEmu_Traits), sizeof(unsigned __int32));
    }
}

BOOL FlsEmu_MapView(FlsEmu_Traits * traits, unsigned __int32 offset, unsigned __int32 length)
{
    DWORD error;
    MEMORY_BASIC_INFORMATION  info;

    assert((offset % pageSize) == 0);   /*  Offset must be a multiple of the allocation granularity! */

    VirtualQuery(traits->persistentArray->mappingAddress, &info, sizeof(MEMORY_BASIC_INFORMATION));


    error = UnmapViewOfFile(traits->persistentArray->mappingAddress);
    if (error == 0UL) {
        error = GetLastError();
        printErrorMessage(L"FlsEmu_MapView", error);
        CloseHandle(traits->persistentArray->mappingHandle);
        return FALSE;
    }
    error = FlushViewOfFile(traits->persistentArray->mappingAddress, info.RegionSize);
    FlushFileBuffers(traits->persistentArray->fileHandle);

    traits->persistentArray->mappingAddress = (void *)MapViewOfFile(traits->persistentArray->mappingHandle, FILE_MAP_ALL_ACCESS, 0, offset, length);
    if (traits->persistentArray->mappingAddress == NULL) {
        error = GetLastError();
        printErrorMessage(L"FlsEmu_MapView", error);
        CloseHandle(traits->persistentArray->mappingHandle);
        return FALSE;
    }
    return TRUE;
}

void FlsEmu_SelectPage(FlsEmu_Traits * traits, unsigned __int8 page)
{
    unsigned __int32 offset;

    if (traits->persistentArray->currentPage == page) {
        return; /* Noting to do. */
    }
    offset = (traits->pageSize * page);
    if (FlsEmu_MapView(traits, offset, traits->pageSize)) {

    }
}

void FlsEmu_SelectBlock(FlsEmu_Traits * traits, unsigned __int8 block)
{
    unsigned __int32 offset, blockSize;

    blockSize = (traits->memSize / traits->blockCount);
    offset = (blockSize * block);

     if (FlsEmu_MapView(traits, offset, blockSize)) {

    }
}

void FlsEmu_EraseSector(FlsEmu_Traits * traits, unsigned __int32 address)
{
    unsigned __int32 mask = (unsigned __int32)traits->sectorSize - 1UL;
    unsigned __int16 * ptr = (unsigned __int16 *)traits->persistentArray->mappingAddress;

    if ((address & mask) != 0UL) {
        // TODO: warn misalignment.
        // ("address (%#X) should be aligned to %u-byte sector boundary.", address, traits->sectorSize)
    }
    
    FillMemory(ptr + (address & ~mask), traits->sectorSize, traits->erasedValue);
}


void FlsEmu_ErasePage(FlsEmu_Traits * traits, unsigned __int8 page)
{
    unsigned __int8 * ptr = (unsigned __int8 * )FlsEmu_BasePointer(&S12D512FlashArray);

    FillMemory(ptr + (traits->pageSize * page), traits->pageSize, traits->erasedValue);
}


void FlsEmu_EraseBlock(FlsEmu_Traits * traits, unsigned __int8 block)
{
    /* TODO: Nur den entsprechenden Block mappen!!! */
    unsigned __int8 * ptr;
    unsigned __int16 offset, blockSize;

    assert(block < (traits->blockCount));

    blockSize = (traits->memSize / traits->blockCount);
    offset = (blockSize * block);

    ptr = (unsigned __int8 * )FlsEmu_BasePointer(&S12D512FlashArray) + offset;

    FillMemory(ptr, blockSize, traits->erasedValue);
}

void FlsEmu_Close(FlsEmu_Traits * traits)
{
    ClosePersitentArray(traits->persistentArray);
    free(traits->persistentArray);
}


/*
** Globale Funktionen.
*/
void printErrorMessage(wchar_t const * func, DWORD error)
{
    wchar_t * messageBuffer = NULL;

    FormatMessage(FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM, NULL, error, 
        0/*MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT)*/, (LPWSTR)&messageBuffer,0, NULL
    );

    if (messageBuffer != NULL) {
        wprintf_s(L"%s failed with: ", func);
        wprintf_s(messageBuffer);

        LocalFree(messageBuffer);
    }
}

DWORD getPageSize(void)
{
    SYSTEM_INFO info;

    GetSystemInfo(&info);
    return info.dwPageSize;
}

DWORD getAllocationGranularity(void)
{
    SYSTEM_INFO info;

    GetSystemInfo(&info);
    return info.dwAllocationGranularity;
}

void Fls_Test(void)
{
    int idx;
    unsigned __int8 * ptr;
 
    pageSize = getPageSize();
    allocationGranularity = getAllocationGranularity();

    FlsEmu_Create(&S12D512EEPROMArray);
    FlsEmu_Create(&S12D512FlashArray);

    for (idx = 0; idx < S12D512FlashArray.blockCount; ++idx) {
        FlsEmu_EraseBlock(&S12D512FlashArray, idx);
    }

    FlsEmu_SelectPage(&S12D512FlashArray, 2);
    FlsEmu_SelectPage(&S12D512FlashArray, 5);
    ptr = (unsigned __int8 *)FlsEmu_BasePointer(&S12D512FlashArray);
    for (idx = 0; idx <= S12D512FlashArray.pageSize; ++idx) {

    }

    FlsEmu_Close(&S12D512EEPROMArray);
    FlsEmu_Close(&S12D512FlashArray);
}
