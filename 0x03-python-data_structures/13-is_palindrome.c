#include "lists.h"
#include <stdio.h>
/**
 *is_palindrome- Checks if linked list is palindrome
 *
 *@head: Linked list
 *
 *Return: 1 if linked list, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
listint_t *n;
int count = 0;
int list[100];
int half, i;
int result = 1;
if (head == NULL || *head == NULL)
{
return (1);
}

n = *head;
while (n != NULL)
{
list[count] = n->n;
n = n->next;
count++;
}

half = count / 2;

for (i = 0; i < half; i++)
{
count--;
if (list[i] != list[count])
{
result = 0;
}
}
return (result);
}
