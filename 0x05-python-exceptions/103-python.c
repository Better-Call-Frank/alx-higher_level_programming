#include <Python.h>
#include <stdio.h>
#include <floatobject.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        const char *type = Py_TYPE(element)->tp_name;

        printf("Element %ld: %s\n", i, type);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid PyBytesObject\n");
        return;
    }

    Py_ssize_t size = PyBytes_GET_SIZE(p);
    char *str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", (size < 10) ? size + 1 : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02hhx", str[i]);
        if (i == 9 || i == size - 1)
            break;
        printf(" ");
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid PyFloatObject\n");
        return;
    }

    double value = PyFloat_AS_DOUBLE(p);

    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}

