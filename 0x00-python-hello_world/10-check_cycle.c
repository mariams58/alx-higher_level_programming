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

	if (list == NULL)
		return (0);
	while(list != NULL)
	{
		list = list->next;
		if (list == tmp)
			return(1);
	}
	return (0);
	free(tmp);
}
