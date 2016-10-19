#include <stdio.h>

int main(void)
{
	int a = 17, b = 4, c, d, e;

	c = a + b;
	d = a / b;
	e = a % b;
	printf("%d + %d = %d\n", a , b, c);
	printf("%d / %d = %d\n", a , b, d);
	printf("%d %% %d = %d\n", a , b, e);
}
