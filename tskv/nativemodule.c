/*
 * nativemodule.c
 * Python bindings for TSKV file format implementation in C.
 * Daniel Bershatsky <daniel.bershatsky@skolkovotech.ru>
 */

#include <Python.h>
#include "native.h"

static PyMethodDef tskv_methods[] = {
    {NULL, NULL, 0, NULL},
};

static PyModuleDef tskv_module = {
    PyModuleDef_HEAD_INIT,
    "native",
    "put doc string here",
    -1,
    tskv_methods,
};

PyMODINIT_FUNC PyInit_native(void) {
	PyObject *module = PyModule_Create(&tskv_module);

    if (!module) {
        return NULL;
    }

    return module;
}
