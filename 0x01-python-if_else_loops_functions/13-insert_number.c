#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *prev, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	current = prev = *head;
	while (current != NULL)
	{
		if (number < current->n)
		{
			break;
		}
		prev = current;
		current = current->next;
	}
	new->n = number;
	new->next = current;
	prev = new;
	return (new);
}
