#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints python list info
 * @p: Pyobjext
 *
 */
void print_python_list_info(PyObject *p)
{
		long int size = PyList_Size(p);
		int i;
		PyListObject *objs = (PyListObject *)p;

		printf("[*] Size of the Python List = %li\n", size);
		printf("[*] Allocated = %li\n", objs->allocated);
		for (i = 0; i < size; i++)
		{
				printf("Element %i: %s\n", i, Py_TYPE(objs->ob_item[i])->tp_name);
		}
}
