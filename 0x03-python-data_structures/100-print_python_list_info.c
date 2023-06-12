#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to a PyObject
 * Return: nothing
 **/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyListObject *list = (PyListObject *)p;
	PyObject *item;
	const char *type;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", (int)size);
	printf("[*] Allocated = %d\n", (int)alloc);

	for (i = 0; i < size; ++i)
	{
		item = list->ob_item[i];
		type = item->ob_type->tp_name;

		printf("Element %d: %s\n", (int)i, type);
	}
}
