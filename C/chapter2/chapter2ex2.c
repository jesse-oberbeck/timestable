#include <stdio.h>


int main(void)
{
	int x = 5, y = 10, r = 7, z = 12;

	x = x + y++;
	printf("%d %d\n", x, y);

	r += ++z;
	printf("%d %d\n", r, z);

	puts("break");

	int a = 5, b = -5;

	printf("%d\n", a + b ? a + b : a - b);
}
