#include <stdio.h>

int main(void)
{
	int a = 5, b = 10;
	double x = 25.5, y = 20;
	int sum = a + b, prod = a * b;
	double secondsum = x + y, secondprod = x * y;
	printf("sum: %d, prod: %d\n", sum, prod);
	printf("double sum:%f prod:%f\n", secondsum, secondprod);
	
}
