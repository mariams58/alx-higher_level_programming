#include "lists.h"
/**
  * check_cycle - checks if a given linked list has a cycle
  * @list: the given entry to the list
  *
  * Return: Always 0 success
  */
int check_cycle(listint_t *list)
{
	listint_t * tmp = list;
	listint_t *next;

	while(list != NULL)
	{
		next = list->next;
		if (next == tmp)
			return (1);
		list = next;
	}
	return (0);
	free(tmp);
	free(next);
}
