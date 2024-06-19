#include "lists.h"

/**
 * check_cycle - checks wether a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 *
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return 1;
		}
	}

	return 0;
}
