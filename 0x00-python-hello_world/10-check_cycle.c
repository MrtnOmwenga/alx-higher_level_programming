#include "lists.h"

/**
 *check_cycle- Checks for cycle in linked list
 *
 *@list: Linked list
 *
 *Return: 0 if no cycle else 1
 */


int check_cycle(listint_t *list)
{
struct listint_s *a;
struct listint_s *b;

a = list;
while (a->next != NULL)
{
b = a-> next;
while (b->next != NULL)
{
if (a == b->next)
{
return (1);
}
b = b->next;
}
a = a->next;
}
return (0);
}
