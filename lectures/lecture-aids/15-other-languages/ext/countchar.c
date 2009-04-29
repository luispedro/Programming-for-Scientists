#include <Python.h>

PyObject* countchar(PyObject* self, PyObject* args) {
    const char* string;
    char ch;
    if (!PyArg_ParseTuple(args,"sc",&string,&ch))
        return NULL;
    int res = 0; 
    while (*string) {
        if (ch == *string) ++res;
        ++string;
    }
    return Py_BuildValue("i", res);
}
static PyMethodDef methods[] = {
    {"countchar",  countchar, METH_VARARGS,
            "countchar(str,ch)\n"
            "Counts the number of ..."},
    {NULL, NULL, 0, NULL} /* Sentinel */
};

PyMODINIT_FUNC initcountchar(void)
{
    (void) Py_InitModule("countchar", methods);
}

