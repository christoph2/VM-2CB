#include <Python.h>
#include <stdio.h>

PyMODINIT_FUNC initexamp(void)
{
    PyObject *m;
        
    m = Py_InitModule( "examp", NULL );
    printf("Hello from C-extension.\n");
} 
