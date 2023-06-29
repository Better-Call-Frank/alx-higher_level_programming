#!/usr/bin/python3

#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    size = PyList_Size(p);
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes;
    PyObject *repr;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes = PyBytes_AsString(p);
    repr = PyObject_Repr(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes);
    printf("  first %ld bytes: ", size + 1);

    if (size >= 10)
        size = 10;

    for (i = 0; i < size; i++) {
        printf("%02hhx", bytes[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");

    Py_DECREF(repr);
}
