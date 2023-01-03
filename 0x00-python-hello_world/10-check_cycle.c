#include "lists.h"
/**
  * check_cycle - checks if a given linked list has a cycle
  * @list: the given entry to the list
  *
  * Return: Always 0 success
  */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (list == NULL|| list->next == NULL)
		return (0);
	tmp = list->next;
	while(list != NULL && tmp->next != NULL)
	{
		list = list->next;
		tmp = (tmp->next)->next;
		if (list == tmp)
			return (1);
	}
	return (0);
	free(tmp);
}
