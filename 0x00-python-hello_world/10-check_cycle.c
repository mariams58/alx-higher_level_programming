#include "lists.h"
/**
  * check_cycle - checks if a given linked list has a cycle
  * @list: the given entry to the list
  *
  * Return: Always 0 success
  */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *head;

	if (list == NULL|| list->next == NULL)
		return (0);
	head = list
	tmp = list->next;
	while(head != NULL && tmp->next != NULL)
	{
		if (head == tmp)
			return(1);
		head = head->next;
		tmp = tmp->next->next;
	}
	return (0);
	free(tmp);
	free(head);
}
