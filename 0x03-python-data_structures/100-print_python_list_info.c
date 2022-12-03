#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - print python
 * @p: input
 */

void print_python_list_info(PyObject *p)
{
unsigned int i;
unsigned int len;
unsigned int allocated;
PyTypeObject *type;
const char *name;

if (p == NULL)
{   
return;
}
len = (unsigned int) PyList_Size(p);
allocated = (unsigned int) ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", len);
printf("[*] Allocated = %d\n", allocated);

for (i = 0; i < len; i++)
{
type = PyList_GET_ITEM(p, i)->ob_type;
name = type->tp_name;
printf("Element %d: %s\n", i, name);
}
}
