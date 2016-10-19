#include <stdio.h>

int main2(void)
{
	puts("A simple function.");
}

int mult(int a, int b)
{
	puts("mult");
	return(a * b);
}

int main(void)
{
	int a = 5, b = 10;
	int c = a + b;
	printf("a: %d b: %d c: %d\n", a, b, c);
	main2();
	printf("result of mult: %d\n", mult(a , b));
}
