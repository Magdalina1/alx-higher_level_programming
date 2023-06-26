#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	Py_ssize_t i;

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *typeName = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, typeName);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t maxSize = size < 10 ? size : 10;

	printf("[*] Python bytes info\n");
	printf("[*] Size of the bytes object = %ld\n", size);
	printf("Trying string: %s\n", PyBytes_AsString(p));
	printf("First %ld bytes: ", maxSize);
	Py_ssize_t i;

	for (i = 0; i < maxSize; i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}
	printf("[*] Python float info\n");
	printf("[.] value: %.17g\n", ((PyFloatObject *)p)->ob_fval);
}
