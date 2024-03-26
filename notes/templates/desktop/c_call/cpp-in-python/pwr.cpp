#include <python3.11//Python.h>

///////////////// actual C++ function /////////////////

class Pwr
{

public:
    Pwr();
    int calc_pwr(int x, int y);
};

Pwr::Pwr(){}

int Pwr::calc_pwr(int x, int y){
    int res = 1;

    for (int i=0;i<y;i++) {
        res = res * x;
    }

    return res;
}

///////////////// Python wrapper /////////////////

static PyObject* pwr_calc(PyObject* self, PyObject* args){
    int vx, vy, ret;

    if(!PyArg_ParseTuple(args,"ii",&vx,&vy)) return NULL;

    Pwr *pwr = new Pwr();
    ret = pwr->calc_pwr(vx, vy);

    return Py_BuildValue("i",ret);
}

static PyMethodDef pwr_calc_mthd[] = {
    {"pwr_calc",pwr_calc,METH_VARARGS,"Get Power Calculation from C++"},
    {NULL,NULL,0,NULL}
};

static struct PyModuleDef pwr_calc_mod = {
    PyModuleDef_HEAD_INIT,
    "powerCalc",
    NULL, -1, pwr_calc_mthd
};

PyMODINIT_FUNC PyInit_powerCalc(){
    return PyModule_Create(&pwr_calc_mod);
}

