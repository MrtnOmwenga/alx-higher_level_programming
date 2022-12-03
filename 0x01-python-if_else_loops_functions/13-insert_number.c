#include "lists.h"
#include <stdlib.h>

/**
 *insert_node- Adds a node to the end of a list
 *
 *@head: Head of the list
 *@number: Data to be added
 *
 *Return: Head of the list
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_head = malloc(sizeof(listint_t));
listint_t *h;
if (new_head == NULL)
{
return (NULL);
}

new_head->n = number;
new_head->next = NULL;

if (*head == NULL)
{
*head = new_head;
}
else
{
h = *head;
while (h->next != NULL)
{
h = h->next;
}
h->next = new_head;
}
return (*head);
}
