#include "lists.h"

int check_(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);
	fast = list;
	slow = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	(
		slow = slow->next;
		fastt = fast->next->next;
		if (slow == fast)
		{
		return (1);
		}
	}
		 
