#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: the PyObject list
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t i;
	PyObject *obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", PyList_Size(p));
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %li: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: the PyBytesObject bytes
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *) p;
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %ld\n", PyBytes_Size(p));
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first %ld bytes: ", PyBytes_Size(p) + 1 > 10 ? 10
				: PyBytes_Size(p) + 1);
		for (i = 0; i < PyBytes_Size(p) + 1 && i < 10; i++)
		{
			printf("%02x ", bytes->ob_sval[i] & 0xff);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
