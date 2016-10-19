#include <stdio.h>
#include <math.h>

int sum_of_squares(int a, int b)
{
	return(pow(a, a) + pow(b, b));
}

int main(void)
{
	int a = 5, b = 6, c;
	c = sum_of_squares(a, b);	//c = 61
	printf("%d\n", c);
}
