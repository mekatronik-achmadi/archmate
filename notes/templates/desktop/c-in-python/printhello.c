#include <stdio.h>
#include <python3.11/Python.h>

// function to call
static PyObject* printhello(PyObject* self, PyObject* args){
    printf("C in Python Template\r\n");
    return Py_None;
}

// method function definition
static PyMethodDef helloMethods[] = {
    {"printhello",printhello,METH_NOARGS,"Print Hello String"},
    {NULL,NULL,0,NULL}
};

// module definition
static struct PyModuleDef helloModule ={
    PyModuleDef_HEAD_INIT,
    "helloModule",
    "hello module",
    -1,
    helloMethods
};

// module initialization
PyMODINIT_FUNC PyInit_helloModule(){
    return PyModule_Create(&helloModule);
}
