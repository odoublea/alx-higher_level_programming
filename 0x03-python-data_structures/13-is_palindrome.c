#include "lists.h"

/**
 * reverse_l - helper to reverse a linked list
 * @head: double ptr to list
 * Return: ptr to the first node of the reversed list
 */

listint_t *reverse_l(listint_t **head)
{
	listint_t *forward = NULL, *previous = NULL;

	while (*head)
	{
		forward = (*head)->next;
		(*head)->next = previous;
		previous = (*head);
		(*head) = forward;

	}

	(*head) = previous;

	return (*head);
}

/**
 * is_palindrome - checks if a singly list is a palindrome
 * @head: ptr to ptr
 * Return: 1 if palindrome or else 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *origin = *head, *reverse = *head;

	if (*head == NULL)
		return (1);

	while (origin->next && origin->next->next)
	{
		reverse = reverse->next;
		origin = origin->next->next;
	}

	reverse = reverse_l(&reverse);
	origin = *head;

	while (origin && reverse)
	{
		if (reverse->n != origin->n)
			return (0);
		origin = origin->next;
		reverse = reverse->next;
	}

	return (1);
}
