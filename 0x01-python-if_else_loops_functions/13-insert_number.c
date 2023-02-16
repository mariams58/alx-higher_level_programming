#include "lists.h"
#include <stdlib.h>
/**
  * insert_node - inserts  a given number in sorted list
  * @head: the head of the linked list given
  * @number: numder to insert
  *
  * Return: node of insertion
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
			new_node->next = NULL;
			*head = new_node;
			return (*head);
			free(new_node->next);
			free(new_node);
	}
	if (*head && number < (*head)->n)
	{
			new_node->next = *head;
			*head = new_node;
			return (*head);
			free(new_node->next);
			free(new_node);
	}
	while (*head != NULL)
	{
		tmp = (*head)->next;
		if ((number > (*head)->n && number < tmp->n) || number == (*head)->n)
		{
			new_node->next = tmp;
			tmp = new_node;
			return (tmp);
		}
		*head = tmp;
	}
	if (number < (*head)->n)
	{
		new_node->next = NULL;
		(*head)->next = new_node;
	}
	return (*head);
	free(new_node->next);
	free(new_node);
}
