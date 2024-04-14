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
	listint_t *ptr = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (list != NULL)
	{
		list = list->next;
		if (ptr == list && ptr->next == list->next)
			return (1);
	}
	return (0);
}
