#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p);
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (pyListObject *)p;

	printf("{*} size of the python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, py_TYPE (obj->ob_item[i])->tp_name);
}
