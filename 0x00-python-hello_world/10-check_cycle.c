#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - checks if a cycle is present in a linked list
  * @head: pointer to the list
  * Return: 0 for Success
  */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list, *tmp = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (ptr != NULL)
	{
		ptr = ptr->next;
		if (tmp == ptr && ptr->next == tmp->next)
			return (1);
	}
	return (0);
}
