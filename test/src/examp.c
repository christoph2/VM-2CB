#include <Python.h>
#include <stdio.h>

PyMODINIT_FUNC initexamp(void)
{
    PyObject *m;
        
    m = Py_InitModule( "examp", NULL );
    printf("\nHello from C-extension.\n");
} 
