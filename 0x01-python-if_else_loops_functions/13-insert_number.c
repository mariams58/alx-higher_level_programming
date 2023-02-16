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
	listint_t *new_node, *temp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	if (*head == NULL)
	{
			new_node->next = NULL;
			new_node->n = number;
			*head = new_node;
			return (*head);
	}
	while (*head != NULL)
	{
		temp = (*head)->next;
		if ((*head)->n < number && temp->n > number)
		{
			new_node->n = number;
			new_node->next = temp;
			temp = new_node;
			return (temp);
			free(new_node->next);
			free(new_node);
		}
		*head = temp;
	}
	new_node->next = NULL;
	new_node->n = number;
	*head = new_node;
	return (*head);
	free(new_node->next);
	free(new_node);
}
