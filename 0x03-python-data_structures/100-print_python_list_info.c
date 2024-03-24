#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(pyobject *p)
{
	long int size = pyList_size(p);
	int i;
	pyListobject *obj = (pyListobject *)p;

	printf("{*} size of the 
