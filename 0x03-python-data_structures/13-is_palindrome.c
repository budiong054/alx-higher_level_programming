#include "lists.h"

listint_t *reverse_listint(listint_t **head);
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *reverse_list;
	listint_t *current;

	current = *head;
	if (*head == NULL)
		return (1);
	reverse_list = reverse_listint(head);
	while (current != NULL)
	{
		if (current->n != reverse_list->n)
			return (0);
		current = current->next;
		reverse_list = reverse_list->next;
	}
	return (1);
}

/**
 * reverse_listint - reverses a listint_t list
 * @head: a pointer to pointer of the first node of listint_t list
 *
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *nextnode, *current, *prevnode;

	prevnode = NULL;
	current = nextnode = *head;
	while (nextnode)
	{
		nextnode = nextnode->next;
		current->next = prevnode;
		prevnode = current;
		current = nextnode;
	}
	current = prevnode;
	return (current);
}
